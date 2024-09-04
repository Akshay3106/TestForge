import streamlit as st


st.title("Contact us")
email = st.text_input("Enter your Email address", value="", max_chars=None, key=None, type='default')
mobile = st.text_input("Enter your mobile number", value="", max_chars=None, key=None, type='default')
message = st.text_area("Enter your message", value="", height=None, max_chars=None, key=None)
st.button("Submit", key=None, help=None)