import streamlit as st

st.title('Contacts')

if 'my_input' not in st.session_state:
    st.session_state['my_input'] = ""
    