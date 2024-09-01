import streamlit as st
from streamlit_folium import st_folium
import folium

st.set_page_config(
    page_title="Impostor Syndrome",
    page_icon="👤",
)

st.header("Early Life of an :red[Impostor]")

st.write("Gieb's early life was nothing special.")
st.write("He was raised by his parents in a small, suburban, and beautiful place of Tuyan in the city of Naga, Cebu, Philippines. He was the youngest of two siblings.")

# Tuyan
m = folium.Map(location=[10.228225133302558, 123.76744527482843], zoom_start=18)
st_folium(m, width=700, height=500)

st.write("He started his studies on a neighboring school (literal neighbor) and transferred to a private catholic school wherein values were instilled in him. For six whole years, he was a good guy all thorugh.")

st.markdown("<br>", unsafe_allow_html=True)
st.error("But high school was different.")
st.markdown("<br>", unsafe_allow_html=True)

st.write("All hell break loose when he entered secondary school. Seemingly enrolled in a public school known for its students' intellect and excellence, he was, on the face of it, mid. While he paid it no mind at first, he began to realize that not everything needs to be good.")
st.write(":red[_For a place like that, all he need to do was to survive._]")

st.write("And he did. He survived high school but not without a cost. He completely lost his genuine confidence and always asked himself...")

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("What did he always ponder??"):
        st.toast("_Were my achievements really mine?_", icon="👤")
    
st.markdown("<br>", unsafe_allow_html=True)
st.page_link("pages/4_👾_Present Life.py", label="", icon="👁️")
        

    




