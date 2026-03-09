import streamlit as st
import random

st.markdown("""
<style>
button[kind="primary"] {
background: linear-gradient(45deg,#ff416c,#ff4b2b);
color:white;
border:none;
border-radius:30px;
padding:15px 30px;
font-size:18px;
box-shadow:0 0 20px rgba(255,75,43,0.7);
transition:0.4s;
}
button[kind="primary"]:hover{
transform:scale(1.1);
box-shadow:0 0 40px rgba(255,75,43,1);
}
</style>
""", unsafe_allow_html=True)

st.title("🎮 Rock Paper Scissors Game")

choices=["Rock","Paper","Scissor"]

if "player" not in st.session_state:
    st.session_state.player=0
    st.session_state.computer=0

col1,col2,col3=st.columns(3)

user_choice=None

with col1:
    if st.button("🪨 Rock",type="primary"):
        user_choice="Rock"

with col2:
    if st.button("📄 Paper",type="primary"):
        user_choice="Paper"

with col3:
    if st.button("✂️ Scissor",type="primary"):
        user_choice="Scissor"

if user_choice:
    computer=random.choice(choices)

    st.write("You:",user_choice)
    st.write("Computer:",computer)

    if user_choice==computer:
        st.info("Tie 😁")
    elif (user_choice=="Rock" and computer=="Scissor") or \
         (user_choice=="Paper" and computer=="Rock") or \
         (user_choice=="Scissor" and computer=="Paper"):
        st.success("You Win 🎉")
        st.session_state.player+=1
    else:
        st.error("Computer Wins 💻")
        st.session_state.computer+=1

st.write("Player Score:",st.session_state.player)
st.write("Computer Score:",st.session_state.computer)