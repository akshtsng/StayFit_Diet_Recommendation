import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Diet Recommendation System!")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    A diet recommendation web application as a part of StayFit web application.
    Made by Akshat Singh, Baibhav Chel, Prathik P, R Sambhavi
    """
)

if st.button("Diet Recommendation"):
    js = "window.open('https://diet-recommendation-system.streamlit.app/Diet_Recommendation', '_blank')"
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)
