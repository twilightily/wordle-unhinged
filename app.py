import streamlit as st

st.set_page_config(
    #page_title="Wordle UNHINGED : Home",
    initial_sidebar_state = "collapsed"
)

#st.title(":yellow[Wordle UNHINGED.]")

def add_glow_effect():
    st.markdown(
        """
        <style>
        .glowing-title {
            font-size: 80px;
            color: #fff;
            text-align: left;
            /* The text-shadow property creates the glow effect */
            text-shadow: 0 0 10px #f1c232, 0 0 20px #f1c232;
            /* Optional: Add animation for a pulsing glow */
            animation: glow 1.0s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from {
                text-shadow: 0 0 10px #f1c232, 0 0 20px #f1c232, 0 0 30px #f1c232, 0 0 40px #f1c232;
            }
            to {
                text-shadow: 0 0 20px #f1c232, 0 0 30px #f1c232, 0 0 40px #f1c232, 0 0 50px #f1c232;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to inject the CSS
add_glow_effect()

# Display the title using the custom CSS class
st.markdown('<h1 class="glowing-title">Wordle UNHINGED.</h1>', unsafe_allow_html=True)

st.markdown("""
<style>
.glow {
    font-size: 80px;
    color: #fff;
    text-align: left;
    /* The text-shadow property creates the glow effect */
    text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #16537e, 0 0 40px #16537e;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="glow">Welcome to Wordle, but UNHINGED :D</p>', unsafe_allow_html=True)

st.write("Here's some ground rules:")
st.write("1. You will get a random word from the mode you've chosen and you've gotta :yellow[guess it]")
st.write("2. When you enter a guess, you'll know what letters are in the :green[right place]")
st.write("3. You will also know how many of the guessed letters are :yellow[right BUT in the wrong place] (if any)")
st.write("3. You will get :red[SIX] chances and the length of your word can be anything.")
st.write(":yellow[ARE YOU READY!?] (p.s. on phone please rotate")

if st.button("PLAY",type='primary',width = 200):
    st.switch_page('pages/mode_pick.py')