import streamlit as st
import random 

random_list=['BARK', 'MEOW', 'DISK', 'LOST', 'WORD', 'POEM', 'FACT', 'GIRL', 'TOWN', 'LOVE', 'DIRT', 'RANT', 'NEWS', 'BIRD', 'ARMY', 'MILK', 'LILY', 'NODE', 'SHOT', 'HEAT', 'RACE', 'DEBT', 'FADE', 'BEAN', 'MEAL', 'POUR', 'FIRE', 'HANG', 'CAGE', 'TAKE', 'PACK', 'WAKE', 'TRIP', 'HALF', 'CROP', 'PACE', 'RUNG', 'DORM', 'GROW', 'TIDY', 'PLOT', "MEADOW", "CRYSTAL", "FOREST", "MIRACLE", "HARVEST", "SHADOW", "GALAXY", "VISIBLE", "PLAYFUL", "CAPTURE", "MOVIE", "FANTASY", "QUALITY", "JOURNEY", "SPIRIT", "ANCIENT", "TOWER", "TEMPLE", "CLASSIC", "MISSION", "BALANCE", "EXPLORE", "AUDIO", "TACTIC", "PATTERN", "ORCHARD", "MEANING", "REFLECT", "SUNRISE"]
# index_of_word = random.randrange(0, len(random_list))
#secret_word = (random_list[index_of_word]).upper
# n=len(secret_word)

st.set_page_config(page_title="Wordle UNHINGED : Random", layout="centered")
st.markdown("<h1 style='text-align: center;'>Wordle UNHINGED.</h1>", unsafe_allow_html=True)
st.markdown("""
<style>
/* Input text color */
input {
    color: yellow !important;
    font-weight: bold;
    background-color: #222 !important;
    border: 1px solid #555 !important;
}
</style>
""", unsafe_allow_html=True)

#setting the secret word so it doesn't change at every rerun
if "secret_word" not in st.session_state:
    st.session_state.secret_word = random.choice(random_list)
n = len(st.session_state.secret_word)

#setting the grid for the words with n columns and 6 chances
if "grid" not in st.session_state:
    st.session_state.grid = [["" for columns in range(n)] for rows in range(6)]

#colors of each of the boxes
if "colours" not in st.session_state:
    st.session_state.colours = [["#3a3a3c" for columns in range(n)] for rows in range(6)]

if "current_row" not in st.session_state:
    st.session_state.current_row = 0

if "current_word" not in st.session_state:
    st.session_state.current_word = ""

if "animate" not in st.session_state:
    st.session_state.animate = False

#initialising the keyboard colors
if "kb_colours" not in st.session_state:
    st.session_state.kb_colours = {ch: "#818384" for ch in "QWERTYUIOPASDFGHJKLZXCVBNM"}

def evaluate_guess(word):
    result_colours = ["gray"] * n
    yellow_letters = 0
    not_green_secret_word=[]
    not_green_x=[]

    # saving correct letters as green
    for i in range(n):
        if word[i] == st.session_state.secret_word[i]:
            result_colours[i] = "green"
        else:
            not_green_secret_word.append(st.session_state.secret_word[i])
            not_green_x.append(word[i])
        
        for letter in not_green_secret_word:
                if letter in not_green_x:           # meaning if letter is yellow
                    yellow_letters += 1
                    not_green_secret_word.remove(letter)    # to handle repeated letterssss

    st.write('{} letters of your guess are right,but in the wrong place'.format(yellow_letters))


    # changing keyboard colours
    for i, ch in enumerate(word):
        if result_colours[i] == "green":
            st.session_state.kb_colours[ch] = "#538d4e"
        else:
            st.session_state.kb_colours[ch] = "#3a3a3c"

    return ["#538d4e" if c == "green" else "#3a3a3c" for c in result_colours]

# printing in the grid
def show_in_grid():
    word = st.session_state.current_word.upper()
    tile_colours = evaluate_guess(word)
    row = st.session_state.current_row

    for i, ch in enumerate(word):
        st.session_state.grid[row][i] = ch
        st.session_state.colours[row][i] = tile_colours[i]

    # starting the next chance
    st.session_state.current_row += 1
    st.session_state.current_word = ""
    st.session_state.animate = False

# taking user input and submitting
input_guess = st.text_input(f"Enter a {n}-letter word:")
if st.button("Submit Word"):
    if len(input_guess) == n and input_guess.isalpha():
        st.session_state.current_word = input_guess.upper()
        st.session_state.animate = True
        st.rerun()
    else:
        st.error(f"Please enter a valid {n}-letter word.")

if st.session_state.animate:
    show_in_grid()

# checking if user has won or lost
if st.session_state.current_row > 0:
    last_row = st.session_state.current_row - 1
    guessed_word = "".join(st.session_state.grid[last_row])

    if guessed_word == st.session_state.secret_word:
        st.success("Congratulations! You guessed the word!! ⭐⭐⭐⭐⭐")
        c1,c2= st.columns(2,gap=None)
        with c1:
            if st.button('PLAY AGAIN'):
                st.session_state.clear()
                st.rerun()
        with c2:
            if st.button('HOME'):
                st.session_state.clear()
                st.switch_page('app.py')
                st.rerun()
        #st.stop()
        

    elif st.session_state.current_row >= 6:
        st.error(f"You lost😈! The word was {st.session_state.secret_word}.")

        c1,c2= st.columns(2,gap=None)
        with c1:
            if st.button('PLAY AGAIN'):
                st.session_state.clear()
                st.rerun()
        with c2:
            if st.button('HOME'):
                st.session_state.clear
                st.switch_page('app.py')
                st.rerun()
        #st.stop()

def tile_html(bg, letter):
    return f"""
    <div style="
        width: 55px; height: 55px;
        background:{bg};
        border-radius: 8px;
        border: 2px solid #444;
        font-size: 32px;
        font-weight: bold;
        text-transform: uppercase;
        colour: white;
        display: flex; align-items: center; justify-content: center;
        margin: 3px;
    ">
        {letter}
    </div>
    """
st.write("")

# creating each tile and giving its respective colour
for r in range(6):
    cols = st.columns(n)  
    for c in range(n):
        letter = st.session_state.grid[r][c]
        col = st.session_state.colours[r][c]
        cols[c].markdown(tile_html(col, letter), unsafe_allow_html=True)


# creating on-screen keyboard display
st.write("")
keyboard_rows = ["ABCDEFGHI", "JKLMNOPQR", "STUVWXYZ"]

for row in keyboard_rows:
    cols = st.columns(len(row),gap=None)
    for i, key in enumerate(row):
        cols[i].markdown(
            f"""
            <div style="
                width: 40px;
                padding: 10px 0;
                text-align: center;
                margin: 3px;
                background: {st.session_state.kb_colours[key]};
                colour: white;
                font-weight: bold;
                border-radius: 6px;
            ">
                {key}
            </div>
            """,
            unsafe_allow_html=True
        )