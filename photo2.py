import pixellib
from pixellib.tune_bg import alter_bg
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
def app2(f1):
    st.title("Black and white image background")


    if st.button("Tune your Image"):
        change_bg = alter_bg(model_type = "pb")
        change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
        st.write("Original Image")
        st.image(f1)
        change_bg.gray_bg(f1.name,output_image_name="gray_img.jpg", detect = "person")
        st.write("Gray Image")
        st.image("gray_img.jpg")
    else:
        st.markdown("** Searching for an image **")
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_MVTGfa.json")
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
