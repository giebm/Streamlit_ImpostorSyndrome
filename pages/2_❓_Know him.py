import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Impostor Syndrome",
    page_icon="👤",
)
# Game Chart
def game_chart():
    labels = 'LOL', 'Valorant', 'Others'
    sizes = [40, 30, 30]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
    
    st.pyplot(fig1)

# Sports Chart
def sports_chart():
    labels = 'Volleyball', 'Badminton', 'Others'
    sizes = [20, 70, 10]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%', startangle=90)
    
    st.pyplot(fig1)

st.markdown("<br><br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col2:
    st.image("mier_oa.png", caption="Impostor")
    
st.markdown("<br>", unsafe_allow_html=True)

st.write("Suspected victim goes by the name of France Gieb S. Mier, mostly called :red[Gieb]. He has lived in Cebu for his whole life of 21 years.")
st.write("He likes playing online games. He loves listening to music. He likes playing sports. He loves being alone.")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    game_chart()
    st.caption("Games Played by Frequency")
with col2:
    st.image("nicole.jpg")
    st.caption("His Favorite Album, _Nicole_")
with col3:
    sports_chart()
    st.caption("Sports Played by Frequency")
    
st.markdown("<br>", unsafe_allow_html=True)
    
st.audio("before.mp3", format="audio/mp3")
st.caption("His Favorite Song, _Before_")

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
    st.write("He was reaaaally no one special.")

st.markdown("<br><br>", unsafe_allow_html=True)

st.error(":red[_But why was he an imposter?_]")

# chat messages
messages = st.container(height=300)
messages.chat_message("assistant").write("Do you want to know why was he an impostor?")
answer = "Good choice. Click the 👁️."

if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"{answer}")
    st.balloons()


st.page_link("pages/3_👁️_Early Life.py", label="", icon="👁️")