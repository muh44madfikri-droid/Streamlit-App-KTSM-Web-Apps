import streamlit as st

st.set_page_config(
    page_title="Karang Taruna Suko Manunggal",
    layout="wide"
)

# ===== STYLE =====
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
.title {
    font-size: 48px;
    font-weight: bold;
    color: #1e293b;
}
.subtitle {
    font-size: 20px;
    color: #475569;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ===== HERO =====
st.markdown('<p class="title">KARANG TARUNA SUKO MANUNGGAL</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Guyub Rukun, Sesarengan Mbangun, Suko Manunggal Maju</p>', unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns([2,1])

with col1:
    st.write("""
    Para pemuda-pemudi RT 13, RT 14, lan RT 20 Dukuh Bandungan ingkang kompak, rukun, lan siyap nyengkuyung kemajuan lingkungan. Dados wadah kanggé sesrawungan, silaturahmi, lan makarya bebarengan. Wiwit saking kerja bakti, kegiatan sosial, ngantos acara sanesipun ingkang migunani, sedaya dipun lampahi kanthi guyub rukun lan gotong royong.
    """)

with col2:
    st.info("📢 Gunakan menu di sidebar untuk navigasi")

st.divider()

# ===== STATISTIK =====
# st.subheader("📊 Statistik")

# col1, col2, col3 = st.columns(3)

# col1.markdown('<div class="card"><h2>34</h2><p>Anggota</p></div>', unsafe_allow_html=True)
# col2.markdown('<div class="card"><h2>5</h2><p>Kegiatan</p></div>', unsafe_allow_html=True)
# col3.markdown('<div class="card"><h2>2025</h2><p>Berdiri</p></div>', unsafe_allow_html=True)

# st.write("")

# ===== KEGIATAN =====
# st.subheader("📌 Kegiatan Utama")

# col1, col2, col3 = st.columns(3)

# col1.markdown('<div class="card">🎉<br><b>Arisan Bulanan</b><br>Kegiatan rutin setiap bulan</div>', unsafe_allow_html=True)
# col2.markdown('<div class="card">🧹<br><b>Kerja Bakti</b><br>Gotong royong lingkungan</div>', unsafe_allow_html=True)
# col3.markdown('<div class="card">🤝<br><b>Kegiatan Sosial</b><br>Bantuan & kegiatan masyarakat</div>', unsafe_allow_html=True)

# st.divider()

# ===== CTA =====
st.subheader("🚀 Akses Sistem")

col1, col2 = st.columns(2)

with col1:
    if st.button("Masuk ke Sistem Arisan"):
        st.switch_page("pages/ArisanApps.py")

with col2:
    if st.button("Masuk tab Pengurus"):
        st.switch_page("pages/Pengurus.py")
st.subheader("🖼️ Dokumentasi Kegiatan")

st.markdown("""
<style>
.gallery-card {
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 15px;
}
.gallery-caption {
    padding: 8px;
    text-align: center;
    font-size: 14px;
    color: #334155;
}
</style>
""", unsafe_allow_html=True)

# Baris 1
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto1.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Logo KTSM</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto2.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Ketua Rabi bolo</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto3.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Kegiatan 3</div></div>', unsafe_allow_html=True)

# Baris 2
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto4.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Kegiatan 4</div></div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto5.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Kegiatan 5</div></div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="gallery-card">', unsafe_allow_html=True)
    st.image("assets/foto6.jpg", use_container_width=True)
    st.markdown('<div class="gallery-caption">Kegiatan 6</div></div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("© 2026 Karang Taruna Suko Manunggal - Dibuat dengan Streamlit")
