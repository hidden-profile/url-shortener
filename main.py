import streamlit as st
import pyshorteners as pys
import pyperclip as pyc
#basic elements
#streamlit run main.py -->to run
sh=pys.Shortener()
def copy():
    pyc.copy(surl)
st.markdown("<h1 style='text-align:center'>Url Shorterner </h1>",unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("Enter the url to be shortened")
submit=form.form_submit_button("SHORTEN")
if submit:
    surl=sh.tinyurl.short(url)
    st.markdown(f"<h6 style='text-align:center'>Shortened URL : <br> {surl}</h6>",unsafe_allow_html=True)
    st.button("Copy",on_click=copy)