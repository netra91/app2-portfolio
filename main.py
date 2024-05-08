import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/image.jpeg",width=450)

with col2:
    st.title("Netravati Belagali")
    content="""
    hi my name is netravati belagali, working as assistant professor in computer science and engineering dept in bgmit, mudhol,karnataka.
    totally having 3+ years of teaching experience.
    """
    st.info(content)