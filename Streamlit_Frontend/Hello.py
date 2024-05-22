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
