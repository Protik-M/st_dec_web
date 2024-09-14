import streamlit as st
import random

st.header(f"---Decision Making APP!!!--- :smile:")
st.text("Make Decision In a Modern Way")

txtone =st.text_input("Your 1st Confusion")
txttwo =st.text_input("Your 2nd Confusion")

button=st.button("MAKE YOUR DECISION!")

list = []
list.append(txtone)
list.append(txttwo)
sion=random.choice(list)


st.write("")
if button:
        st.header(f"You Should Use :green[{sion}]")
        
        st.write("APP CODED BY PROTIK M.")
        st.balloons()

        
        


