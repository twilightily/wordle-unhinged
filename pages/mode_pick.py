import streamlit as st
import random

st.set_page_config(
    page_title="Wordle UNHINGED : Pick Mode"
)

st.title(":yellow[What mode would you like to play in]")

st.write("i.e. what set of words would you like to guess (p.s. LOOK we have a :blue[PES MODE]>:D)")
c1,c2,c3,c4 = st.columns(4,gap='small')
secret_word=''

with c1:
    if st.button("PES MODE",type='primary',width = 'stretch'):
            st.switch_page('pages/pes_play.py')

with c2:
    if st.button("FOOD",type='primary',width = 'stretch'):
            st.switch_page('pages/food_play.py')

with c3:
    if st.button("TECH",type='primary',width = 'stretch'):
            st.switch_page('pages/tech_play.py')

with c4:
    if st.button("RANDOM",type='primary',width = 'stretch'):
            st.switch_page('pages/random_play.py')
