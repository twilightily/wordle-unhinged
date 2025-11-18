import streamlit as st

st.set_page_config(
    page_title="Wordle UNHINGED : Home",
    initial_sidebar_state = "collapsed"
)

st.title(":yellow[Wordle UNHINGED.]")

st.markdown("""
<style>
.glow {
    font-size: 80px;
    color: #fff;
    text-align: left;
    /* The text-shadow property creates the glow effect */
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #f5e102, 0 0 40px #f5e102, 0 0 50px #f5e102, 0 0 60px #f5e102, 0 0 70px #f5e102;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="glow">Welcome to Wordle, but UNHINGED :D</p>', unsafe_allow_html=True)

st.write("Here's some ground rules:")
st.write("1. You will get a random word from the mode you've chosen and you've gotta :yellow[guess it]")
st.write("2. When you enter a guess, you'll know what letters are in the :green[right place]")
st.write("3. You will also know how many of the guessed letters are :yellow[right BUT in the wrong place] (if any)")
st.write("3. You will get :red[SIX] chances and the length of your word can be anything.")
st.write(":yellow[ARE YOU READY!?]")

if st.button("PLAY",type='primary'):
    st.switch_page('pages/mode_pick.py')
