import streamlit as st
import Auth


def main():
   

    if st.session_state.username is None:
        Auth.Login()
    else:
        with st.sidebar:
            if st.session_state.logoutG_clicked:
              Auth.logout_Generator()





