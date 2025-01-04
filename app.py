import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secret["genai"])

def get_response(input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!="":
        response=model.generate_content([input,image])
    else:
        input="Explain this image"
        response=model.generate_content([input,image])
    return response.text

def main():
    st.title("Image AI Chatbot")
    st.write("Provide an image and a question and let AI answer it.")

    capture = st.radio("Choose capture mode",("Webcam","Upload"))

    if capture == "Webcam":
        img=st.camera_input(label="",key="webcam")

        if img is not None:
            image = Image.open(img)
            st.image(image,caption="Webcam")
    
    else:
        upload= st.file_uploader("Upload Image",type=["jpg","jpeg","png"])
        if upload is not None:
            image = Image.open(upload)
            st.image(image,caption="Upload")
    
    input = st.text_input("Input prompt:",key = "input")
    submit = st.button("Get Response")

    if submit:
        response = get_response(input,image)
        st.subheader("Response")
        st.write(response)


if __name__ =="__main__":
    main()
