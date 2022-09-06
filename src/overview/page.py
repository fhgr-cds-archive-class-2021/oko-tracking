import streamlit as st


def page():
    st.subheader("Overview page")
    with open("README.md", "r") as f:
        st.markdown(f.read())
