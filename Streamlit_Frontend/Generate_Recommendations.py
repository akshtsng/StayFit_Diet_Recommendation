import streamlit as st

# Streamlit code to create the interface
st.title("Diet Recommendation System")

# Button to generate recommendations
if st.button("Generate Recommendations"):
    js = "window.location.href = 'https://diet-recommendation-system.streamlit.app/Diet_Recommendation';"
    html = '<script>{}</script>'.format(js)
    st.markdown(html, unsafe_allow_html=True)
