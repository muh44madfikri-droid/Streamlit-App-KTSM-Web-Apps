import streamlit as st

st.title("👥 Pengurus")

data = {
    "Ketua": "Saridianto",
    "Wakil Ketua": "Salis Sapudin",
    "Sekretaris": "Muhamad Fikri",
    "Bendahara": "Romi Abidin"
}

for k, v in data.items():
    st.write(f"**{k}** : {v}")
    
# Footer
st.markdown("---")
st.caption("© 2026 Karang Taruna Suko Manunggal - Dibuat dengan Streamlit")
