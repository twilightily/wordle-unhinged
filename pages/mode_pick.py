import streamlit as st
st.title(":yellow[What mode would you like to play in]")
st.write("i.e. what set of words would you like to guess (p.s. LOOK we have a PES MODE >:D)")
c1,c2,c3,c4 = st.columns(4)

with c1:
    if st.button("RANDOM",type='primary'):
            st.write(" clicked!")

with c2:
    if st.button("FOOD",type='primary'):
            st.write("Button 1 clicked!")

with c3:
    if st.button("TECH",type='primary'):
            st.write("Button 1 clicked!")

with c4:
    if st.button("PES MODE",type='primary'):
            st.write("Button 1 clicked!")
