import streamlit as st
import pandas as pd
import Auth
import docs


for key in ['username', 'uploaded_TestPlan', 'uploaded_oldFeatures', 'oldFeature_comment', 'newFeature_comment', 'uploaded_newFeatures','jsonFile']:
    if key not in st.session_state:
        st.session_state[key] = None
if 'test_case_index' not in st.session_state:
    st.session_state.test_case_index = 0
def main():
    

    if st.session_state.username is None:
        Auth.Login()
    else:
        with st.sidebar:
            if st.session_state.logoutM_clicked:
              Auth.logout_modifier()

        testplan_files = docs.testplan(key_suffix="_modifier")
        oldfeatures_comment = docs.oldfeatures()
        newfeatures_comment = docs.newfeatures()

        if testplan_files:
            st.session_state.jsonFile = "jsonFile.json"
            with st.spinner('Processing files...'):
              for file in testplan_files:
                docs.convert_file_to_json(input_file=file,json_file=st.session_state.jsonFile)
            with st.spinner('Generating response...'):
                docs.process_and_convert_to_excel(newfeatures_comment,oldfeatures_comment)
            df = pd.read_excel('formatted_test_cases.xlsx')

             # Display the DataFrame in Streamlit
            st.write("Displaying the Excel Sheet:")
            st.dataframe(df)
        