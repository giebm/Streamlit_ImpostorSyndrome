import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(
    page_title="Impostor Syndrome",
    page_icon="👤",
)

def display_rain():
    rain(
        emoji="🍓",
        font_size=120,
        falling_speed=4,
        animation_length="infinite",
    )

st.header("Where the :red[Impostor] is Now")
st.subheader("Present life, the impostor lives.")

st.markdown("<br>", unsafe_allow_html=True)

st.write("Gieb lives as a student of Bachelor of Science in Information Technology at the Cebu Institute of Technology - University. He is currently on his 4th year of his studies. and still struggling.")

st.markdown("<br>", unsafe_allow_html=True)
code = '''def help():
    print("The Impostor struggles!!!")'''
st.code(code, language="python")
st.caption("_I am really struggling._")
st.markdown("<br>", unsafe_allow_html=True)

st.write("While he regrets that the impostor within him lives, it does not stop him from enjoying his life. He is definitely happy.")

st.markdown("<br>", unsafe_allow_html=True)
st.write("And so the impostor lives—struggling, but happy.")

st.markdown("<br>", unsafe_allow_html=True)
st.write("_Oh, he likes strawberries very much, too._")

if st.button("🍓🍓🍓"):
    display_rain()