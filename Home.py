import streamlit as st
import pandas

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
content2 = """
    Below you can find some of the apps I have built in python. Feel free to contact me!
    """
st.write(content2)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")
