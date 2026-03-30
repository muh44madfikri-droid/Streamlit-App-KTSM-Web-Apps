import streamlit as st
from supabase import create_client
import pandas as pd

# ===== CONFIG =====
SUPABASE_URL = "https://camzjaixmesyylimmqgf.supabase.co"
SUPABASE_KEY = "sb_publishable_HRQ4MrzieFxIp-_U0vtXNQ_VUOpbnj_"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="KTSM", layout="wide")

# ===== LOGIN =====
st.sidebar.title("🔐 Login")

user = st.sidebar.text_input("Username")
pw = st.sidebar.text_input("Password", type="password")

if user != "admin" or pw != "123":
    st.warning("Login dulu")
    st.stop()

# ===== PILIH PERIODE =====
st.sidebar.title("📅 Periode")

bulan_list = [
    "01 - Januari","02 - Februari","03 - Maret","04 - April",
    "05 - Mei","06 - Juni","07 - Juli","08 - Agustus",
    "09 - September","10 - Oktober","11 - November","12 - Desember"
]

bulan = st.sidebar.selectbox("Bulan", bulan_list)
tahun = st.sidebar.selectbox("Tahun", list(range(2025, 2031)))

kode_bulan = bulan.split(" - ")[0]
periode = f"{tahun}-{kode_bulan}"

st.sidebar.success(f"Periode: {periode}")

# ===== FUNCTIONS =====
def load_anggota():
    res = supabase.table("anggota").select("*").execute()
    data = res.data

    if not data:
        return pd.DataFrame(columns=["id","nama"])

    df = pd.DataFrame(data)
    df.columns = [c.lower() for c in df.columns]
    return df

def load_transaksi():
    res = supabase.table("transaksi")\
        .select("*")\
        .eq("periode", periode)\
        .execute()

    data = res.data

    if not data:
        return pd.DataFrame(columns=["anggota_id","periode","bayar","menang"])

    df = pd.DataFrame(data)
    df.columns = [c.lower() for c in df.columns]
    return df

def get_status(anggota_id, transaksi_df):
    row = transaksi_df[transaksi_df["anggota_id"] == anggota_id]

    if row.empty:
        return False, False

    return row.iloc[0]["bayar"], row.iloc[0]["menang"]

def save_transaksi(anggota_id, bayar, menang):
    existing = supabase.table("transaksi")\
        .select("*")\
        .eq("anggota_id", anggota_id)\
        .eq("periode", periode)\
        .execute()

    if existing.data:
        supabase.table("transaksi")\
            .update({
                "bayar": bayar,
                "menang": menang
            })\
            .eq("anggota_id", anggota_id)\
            .eq("periode", periode)\
            .execute()
    else:
        supabase.table("transaksi")\
            .insert({
                "anggota_id": anggota_id,
                "periode": periode,
                "bayar": bayar,
                "menang": menang
            })\
            .execute()

# ===== UI =====
st.title("KARANG TARUNA SUKO MANUNGGAL APPS")

anggota_df = load_anggota()
transaksi_df = load_transaksi()

# ===== STATISTIK =====
total = len(anggota_df)
sudah_bayar = len(transaksi_df[transaksi_df["bayar"] == True])
sudah_menang = len(transaksi_df[transaksi_df["menang"] == True])

col1, col2, col3 = st.columns(3)
col1.metric("Total Anggota", total)
col2.metric("Sudah Bayar", sudah_bayar)
col3.metric("Sudah Menang", sudah_menang)

st.progress(sudah_bayar / total if total else 0)

st.divider()

# ===== DATA ANGGOTA =====
st.subheader(f"📋 Data Anggota - {periode}")

for _, row in anggota_df.iterrows():
    col1, col2, col3 = st.columns([2,1,1])

    bayar, menang = get_status(row["id"], transaksi_df)

    col1.write(row["nama"])

    # BAYAR
    if bayar:
        col2.success("✔")
    else:
        col2.error("✖")

    new_bayar = col2.checkbox(
        "Bayar",
        value=bayar,
        key=f"bayar_{row['id']}"
    )

    # MENANG
    if menang:
        col3.success("🏆")
    else:
        col3.write("-")

    new_menang = col3.checkbox(
        "Menang",
        value=menang,
        key=f"menang_{row['id']}"
    )

    if new_bayar != bayar or new_menang != menang:
        save_transaksi(row["id"], new_bayar, new_menang)

st.divider()

# ===== UNDIAN =====
st.subheader(f"🎲 Undian Periode {periode}")

kandidat = transaksi_df[
    (transaksi_df["bayar"] == True) &
    (transaksi_df["menang"] == False)
]

if st.button("Undi"):
    if len(kandidat) == 0:
        st.warning("Tidak ada kandidat")
    else:
        pemenang = kandidat.sample(1).iloc[0]

        save_transaksi(pemenang["anggota_id"], True, True)

        nama = anggota_df[
            anggota_df["id"] == pemenang["anggota_id"]
        ]["nama"].values[0]

        st.success(f"🎉 Pemenang: {nama}")
        st.balloons()
        st.rerun()

# ===== BELUM BAYAR =====
st.subheader("❌ Belum Bayar")

sudah_bayar_ids = transaksi_df[
    transaksi_df["bayar"] == True
]["anggota_id"]

belum = anggota_df[
    ~anggota_df["id"].isin(sudah_bayar_ids)
]

if len(belum) == 0:
    st.success("Semua sudah bayar 🎉")
else:
    for nama in belum["nama"]:
        st.write(f"- {nama}")
