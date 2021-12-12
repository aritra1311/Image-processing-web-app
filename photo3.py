import pixellib
from pixellib.tune_bg import alter_bg
import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
def app3(f1):
    st.title("Making your own collage")
    count=1
    c = st.number_input(label="Select how many more images you want to add in order to make the collage",step=1,format="%i")
    i=0
    while(i<c):
        f2 = st.file_uploader("Upload Your background Image ",type=["jpg","png","jpeg"],key = count)
        count+=1
        if st.button("Tune your Image",key = count):
            change_bg = alter_bg(model_type = "pb")
            change_bg.load_pascalvoc_model("xception_pascalvoc.pb")
            if(i==0):
                st.write("Original Image")
                st.image(f1)
                change_bg.change_bg_img(f_image_path = f1.name,b_image_path = f2.name, output_image_name="new_img.jpg")
                st.write("New Image")
                st.image("new_img.jpg")
            else:
                st.write("Original Image")
                st.image("new_img.jpg")
                change_bg.change_bg_img(f_image_path = "new_img.jpg",b_image_path = f2.name, output_image_name="new_img.jpg")
                st.write("New Image")
                st.image("new_img.jpg")
        i+=1
