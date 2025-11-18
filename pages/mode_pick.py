import streamlit as st
import random

st.set_page_config(
    page_title="Wordle UNHINGED : Pick Mode",
    initial_sidebar_state = "collapsed"
)

st.title(":yellow[What mode would you like to play in]")

st.write("i.e. what set of words would you like to guess (p.s. LOOK we have a :blue[PES MODE]>:D)")
c1,c2,c3,c4 = st.columns(4,gap=None)
secret_word=''

with c1:
    if st.button("RANDOM",type='primary'):
            # random_list=['BARK','MEOW']
            # index_of_word = random.randrange(0, len(random_list))
            # secret_word = random_list[index_of_word]
            st.switch_page('pages/wordle_ui_final.py')

with c2:
    if st.button("FOOD",type='primary'):
            st.write("Button 1 clicked!")

with c3:
    if st.button("TECH",type='primary'):
            st.write("Button 1 clicked!")

with c4:
    if st.button("PES MODE",type='primary'):
            st.write("Button 1 clicked!")
