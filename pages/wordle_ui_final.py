import streamlit as st

secret_word = "APPLE"
n = len(secret_word)

st.set_page_config(page_title="Wordle UNHINGED.", layout="centered")
st.html("<h1 style='text-align: center;'>Wordle UNHINGED.</h1>")
st.markdown("""
<style>
/* Input text color */
input {
    color: white !important;
    font-weight: bold;
    background-color: #222 !important;
    border: 1px solid #555 !important;
}
</style>
""", unsafe_allow_html=True)


if "grid" not in st.session_state:
    st.session_state.grid = [["" for columns in range(n)] for rows in range(7)]

if "colours" not in st.session_state:
    st.session_state.colours = [["#3a3a3c" for columns in range(n)] for rows in range(7)]

if "current_row" not in st.session_state:
    st.session_state.current_row = 0

if "current_word" not in st.session_state:
    st.session_state.current_word = ""

if "animate" not in st.session_state:
    st.session_state.animate = False

if "kb_colours" not in st.session_state:
    st.session_state.kb_colours = {ch: "#818384" for ch in "QWERTYUIOPASDFGHJKLZXCVBNM"}

def evaluate_guess(word):
    result_colours = ["gray"] * n

    # saving correct letters as green
    for i in range(n):
        if word[i] == secret_word[i]:
            result_colours[i] = "green"

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

    if guessed_word == secret_word:
        st.success("Congratulations! You found the secret word ⭐⭐⭐⭐⭐")
        st.stop()

    if st.session_state.current_row >= 7:
        st.error(f"You lost! The word was {secret_word}.")
        st.stop()

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
for r in range(7):
    cols = st.columns(n)  
    for c in range(n):
        letter = st.session_state.grid[r][c]
        col = st.session_state.colours[r][c]
        cols[c].markdown(tile_html(col, letter), unsafe_allow_html=True)


# creating on-screen keyboard display
st.write("")
keyboard_rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

for row in keyboard_rows:
    cols = st.columns(len(row))
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