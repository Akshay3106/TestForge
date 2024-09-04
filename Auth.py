import streamlit as st  

def Login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login",key="Login"):
        if username == "admin" and password == "password":
            st.session_state.username = username              
        else:
                st.error("Invalid username or password")

def logout_modifier():
    if st.button("Logout",key="logout_modifier"):
      st.session_state.username = None
def logout_Generator():
    if st.button("Logout",key="logout_Generator"):
      st.session_state.username = None