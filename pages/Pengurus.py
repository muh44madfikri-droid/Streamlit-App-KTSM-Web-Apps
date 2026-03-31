import streamlit as st

st.title("👥 Pengurus")

data = {
    "Ketua": "Ryanto",
    "Wakil Ketua": "Salis",
    "Sekretaris": "Muhamad Fikri",
    "Bendahara": "Romi Abidin"
}

for k, v in data.items():
    st.write(f"**{k}** : {v}")
    
# Footer
st.markdown("---")
st.caption("© 2026 Karang Taruna Suko Manunggal - Dibuat dengan Streamlit")
