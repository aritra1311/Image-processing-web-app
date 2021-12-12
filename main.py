import photo1
import photo2
import photo3
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title='Image Edit and Collage Maker')

st.title("** Image Editing and Collage maker **")
st.markdown("** 19BCE1242 Aritra Basu**")
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cznnfmoz.json")
st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)
f1 = st.file_uploader("Upload Your Image ",type=["jpg","png","jpeg"])
PAGES = {

    "Blur your image background": photo1,
    "Black and white image background": photo2,
    "Making your own collage":photo3

}

st.markdown('***')
value = st.selectbox("Select a Functionality", options=list(PAGES.keys()))
page = PAGES[value]

if value == "Blur your image background":
    page.app1(f1)
elif value == "Black and white image background":
    page.app2(f1)
elif value == "Making your own collage":
    page.app3(f1)
