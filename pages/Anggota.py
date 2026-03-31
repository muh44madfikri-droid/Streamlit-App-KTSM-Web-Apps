import streamlit as st

# Pengaturan halaman
st.set_page_config(
    page_title="Data Anggota Karang Taruna",
    page_icon="👥",
    layout="centered"
)

# Judul Utama
st.title("👥 Daftar Anggota Karang Taruna")
st.markdown("---")

# List nama anggota
anggota = [
    "Riskha Andika", "Dimas Santoso", "Romi Abidin", "Muhamad Fikri",
    "Trio Rizky Subekhi", "Septian Angga Dwi Saputra", "Andrea Marchel Dinansyah",
    "Nur Harjuno", "Nanang Eko Santoso", "Roni Hidayat", "Niken Diana Lestari",
    "Suyanto Aditya", "Andra Yani", "Gunawan", "Alpin Alamzah", "Bayu Andrianto",
    "Juwita Maharani", "Yufika Verlyanti", "Heni Nuratin", "Aldino Vairosi Albras",
    "Rangga Damar Riffaif", "Rudy Kristianto", "Dicky Wahyudi", 
    "Anisa Putri Rahma Dayanti", "Salis Sapudin", "Saridianto", "Yahmin",
    "Ryan Dwi Saputra", "Risma Anggita Putri", "Rabela Dwi Agustin",
    "Hariyanto", "Yeni Yupita Sari", "Agung Widodo", "Chindy Aulia"
]

# Fitur Pencarian
search = st.text_input("🔍 Cari nama anggota:", "")

# Filter data berdasarkan pencarian
filtered_anggota = [nama for nama in anggota if search.lower() in nama.lower()]

# Menampilkan statistik singkat
col1, col2 = st.columns(2)
col1.metric("Total Anggota", len(anggota))
col2.metric("Hasil Pencarian", len(filtered_anggota))

st.write("")

# Menampilkan daftar anggota dalam tabel atau list
if filtered_anggota:
    # Menggunakan container agar rapi
    with st.container():
        for i, nama in enumerate(filtered_anggota, 1):
            st.write(f"{i}. {nama}")
else:
    st.warning("Nama tidak ditemukan.")

# Footer
st.markdown("---")
st.caption("© 2026 Karang Taruna Suko Manunggal - Dibuat dengan Streamlit")
