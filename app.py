# -*- coding: utf-8 -*-
"""Deployment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19L6Jo-0yUJofnmFsWnXAsmqpWg36nktG
"""

import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('weights-improvement-16-0.89.hdf5')
    return model

model = load_model()
st.title("🍏🍅 Apples Tomatoes Classifier :)")

file = st.file_uploader("Choose an image of an apple or tomato from your computer", type=["jpg", "png"])

def import_and_predict(image_data, model):
    size = (128, 128)
    image = ImageOps.fit(image_data, size, Image.LANCZOS)
    image = np.asarray(image)
    image = image / 255.0
    img_reshape = np.reshape(image, (1, 128, 128, 3))
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please upload an image file (Apple or Tomato)")
else:
    st.write('Starting a long computation...')
    
