import streamlit as st

st.title(":yellow[Wordle UNHINGED]")

st.write("Welcome to Wordle, but UNHINGED :D")
st.write("Here's some ground rules:")
st.write("1. Works like wordle except this time you won't know which letters are in the wrong place")
st.write("2. Basically you'll know what letters are in the :green[right place], and only HOW MANY letters are :yellow[right but wrong place]")
st.write("3. You will get :green[SEVEN] chances and the length of your can be anything.")
st.write("4. If you do not enter the right amount of letters you will :red[LOSE THAT CHANCE]")
st.write(":yellow[ARE YOU READY!?]")

if st.button("PLAY",type='primary'):
    st.switch_page('pages/mode_pick.py')
