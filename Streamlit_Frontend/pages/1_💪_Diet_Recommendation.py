import streamlit as st

# Title of the application
st.title("Diet Recommendation System")

# Sidebar for navigation
st.sidebar.title("Navigation")

# Navigation button in the sidebar
if st.sidebar.button("Diet Recommendation"):
    js = "window.open('https://diet-recommendation-system.streamlit.app/Diet_Recommendation', '_blank')"
    html = '<script>{}</script>'.format(js)
    st.sidebar.markdown(html, unsafe_allow_html=True)

# Main content
st.write("Welcome to the Diet Recommendation System. Use the navigation to proceed.")
