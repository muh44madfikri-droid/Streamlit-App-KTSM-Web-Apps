import streamlit as st

st.set_page_config(page_title="Profil Karang Taruna", layout="wide")

# Judul
st.title("🤝🏻 Profil Karang Taruna Suko Manunggal")

st.markdown("---")

# Deskripsi utama
st.markdown("""
Para pemuda-pemudi RT 13, RT 14, lan RT 20 Dukuh Bandungan ingkang kompak, rukun, lan siyap nyengkuyung kemajuan lingkungan.

KARANG TARUNA SUKO MANUNGGAL minangka wadah pemuda ingkang gadhah tujuan kanggé nguataken persaudaraan, ngembangaken potensi generasi muda, saha nyengkuyung kegiatan sosial lan kemasyarakatan kanthi semangat gotong royong. Lumantar kebersamaan, kita ngupadi supados pemuda saged langkung aktif, kreatif, lan migunani tumrap masyarakat sakupenge.

Dados papan sesrawungan, silaturahmi, lan makarya bebarengan, sedaya anggota saged sinau, berbagi gagasan, lan ngleksanani kegiatan positif. Wiwit saking kerja bakti, acara pemuda, kegiatan sosial, program kebersihan lingkungan lan ngantos program-program kemasyarakatan sanesipun, sedaya dipun lampahi kanthi guyub rukun lan gotong royong.
""")

st.markdown("---")

# Visi & Misi
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 Visi")
    st.write("""
    Dados organisasi pemuda ingkang solid, mandiri, lan berdaya guna tumrap masyarakat.
    """)

with col2:
    st.subheader("📌 Misi")
    st.write("""
    - Ngiyataken persatuan lan kesatuan pemuda  
    - Ngembangaken kreativitas lan potensi generasi muda  
    - Nyengkuyung kegiatan sosial lan kepedulian lingkungan  
    - Mbangun komunikasi lan koordinasi  
    - Nguri-uri budaya gotong royong  
    """)

st.markdown("---")

# Kegiatan
st.subheader("📌 Kegiatan")
st.write("""
- Kerja bakti lingkungan
- Laden manten
- Gotong royong lelayu  
- Acara pemuda-pemudi      
""")

st.markdown("---")

# Moto
st.subheader("📣 Moto")
st.success('"Guyub Rukun, Sesarengan Mbangun, Suko Manunggal Maju"')

st.markdown("---")

# Sosial media
st.subheader("🎵 Media Sosial")

st.write("TikTok:")
st.markdown("https://www.tiktok.com/@karangtarunasokomanungal")

# Footer
st.markdown("---")
st.caption("© 2026 Karang Taruna Suko Manunggal - Dibuat dengan Streamlit")
