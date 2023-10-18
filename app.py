    # -*- coding: utf-8 -*-
"""Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19L6Jo-0yUJofnmFsWnXAsmqpWg36nktG
"""

import streamlit as st
import tensorflow as tf
import cv2
from PIL import Image,ImageOps
import numpy as np
import time
import pandas as pd

@st.cache_resource
def load_model():
  model=tf.keras.models.load_model('weights-improvement-16-0.89.hdf5')
  return model
model=load_model()
st.title("🍏🍅Apples Tomatoes Classifier :)")
file=st.file_uploader("Choose a image of apple or tomato from your computer",type=["jpg","png"])

def import_and_predict(image_data,model):
    size=(128,128)
    image = ImageOps.fit(image_data,size, Image.LANCZOS)
    image = np.asarray(image)
    image = image / 255.0
    img_reshape = np.reshape(image, (1, 128, 128, 3))
    prediction = model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file (Apple or Tomato)")
else:
    'Starting a long computation...'

    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
    
    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'Iteration {i+1}')
      bar.progress(i + 1)
      time.sleep(0.1)
    
    '...and now we\'re done!'
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Apple', 'Tomato']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)

    st.text_input("Your name", key="name")
    st.session_state.name
    
    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')
    
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns = ['lat', 'lon'])
    st.map(map_data)
    
    if st.checkbox('Show dataframe'):
        chart_data = pd.DataFrame(
           np.random.randn(20, 3),
           columns=['a', 'b', 'c'])
    
        chart_data
