import streamlit as st
import Auth
import Test_Case_Generator
import Test_Case_Modifier
for key in ['username', 'uploaded_TestPlan', 'uploaded_oldFeatures', 'oldFeature_comment', 'newFeature_comment', 'uploaded_newFeatures','jsonFile','logoutM_clicked','logoutG_clicked']:
    if key not in st.session_state:
        st.session_state[key] = None

if 'modifier_clicked' not in st.session_state:
    st.session_state.modifier_clicked = False
    if 'generator_clicked' not in st.session_state:
        st.session_state.generator_clicked = False

def main():
    # Set page configuration with title and icon
    st.set_page_config(page_title="TestForge", page_icon=":hammer:")

    # Sidebar login/logout handling
    if st.session_state.username is None:
        Auth.Login()
    else:
        # Sidebar with logout button and welcome message
        with st.sidebar:
            st.image("https://www.bing.com/th?id=OIP.jQvFuRlmVesA7K6ArjfyrAHaH9&w=150&h=161&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2", width=150)  # Placeholder for user avatar (optional)
            st.header(f"Welcome, {st.session_state.username}!")
            st.subheader("Navigation")

        # Main content area
        st.title("🛠️ TestForge")
        st.subheader("Start Test Case Generation")
        content_placeholder = st.empty()


        # Layout with columns for buttons
        col1, col2 = st.columns(2)

        with col1:
            if st.button("📝 Test Case Modifier", key="modifier"):
                st.session_state.modifier_clicked = True
                st.session_state.generator_clicked = False  # Reset other button state
            if st.session_state.modifier_clicked:
                Test_Case_Modifier.main()

        # Handle Test Case Generator button
        with col2:
            if st.button("⚙️ Test Case Generator", key="generator"):
                st.session_state.generator_clicked = True
                st.session_state.modifier_clicked = False  # Reset other button state
            if st.session_state.generator_clicked:
                Test_Case_Generator.main()

         # Display full screen content based on selection
        if st.session_state.modifier_clicked:
            with content_placeholder.container():
                Test_Case_Modifier.main()

        if st.session_state.generator_clicked:
            with content_placeholder.container():
                Test_Case_Generator.main()

        # Add a nice visual separation
        st.markdown("---")
        st.info("Choose an action to start working with test cases.")

if __name__ == "__main__":
    main()
