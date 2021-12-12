import pixellib
from pixellib.tune_bg import alter_bg
import streamlit as st
import json
import requests
import io
import numpy as np
import base64
from PIL import Image
from streamlit_lottie import st_lottie
def app1(f1):
    st.title("Blurring your Image background")



    if st.button("Tune your Image"):
        change_bg = alter_bg(model_type = "pb")
        change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
        st.write("Original Image")
        st.image(f1)
        change_bg.blur_bg(f1.name, low = True, output_image_name="blur_img.jpg")
        st.write("Blurred Image")
        st.image("blur_img.jpg")
        

    else:
        st.markdown("** Searching for an image **")
        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_jo7huq2d.json")
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
