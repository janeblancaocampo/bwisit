import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image, ImageOps
import numpy as np

# Function to load the pre-trained model
@st.cache(allow_output_mutation=True)
def load_model():
    model = tf.keras.models.load_model('weights-improvement-10-0.91.hdf5', custom_objects={'KerasLayer': hub.KerasLayer})
    return model

# Set the page title and description
st.set_page_config(page_title="Time of the Day Classification", page_icon="🌞")
st.title("Time of the Day Classification")
st.markdown("---")
st.write("Using the image you've uploaded, this website classifies what time of day it is. The prediction will be either Day Time, Night Time, or Sunrise.")

# File uploader
file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Function to preprocess and predict the image
def import_and_predict(image_data, model):
    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.LANCZOS)
    image = np.asarray(image)
    image = image / 255.0
    img_reshape = np.reshape(image, (1, 224, 224, 3))
    prediction = model.predict(img_reshape)
    return prediction

# Load the pre-trained model
model = load_model()
class_names = ['Day Time', 'Night Time', 'Sunrise']

# Display prediction results
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    prediction = import_and_predict(image, model)
    class_index = np.argmax(prediction)
    class_label = class_names[class_index]
    string = "Prediction: " + class_label
    st.success(string)

# Safety Tips
st.markdown("---")
st.header("Safety Tips")

if class_label == "Day Time":
    st.write("Safety Tips for Day Time:")
    st.write("1. Stay hydrated and drink plenty of water.")
    st.write("2. Use sunscreen to protect your skin from the sun's harmful UV rays.")
    st.write("3. Wear sunglasses to protect your eyes from sunlight.")
elif class_label == "Night Time":
    st.write("Safety Tips for Night Time:")
    st.write("1. Ensure proper lighting in dark areas to prevent accidents.")
    st.write("2. Be aware of your surroundings and stay alert.")
    st.write("3. Use reflective clothing or accessories for visibility.")
elif class_label == "Sunrise":
    st.write("Safety Tips for Sunrise:")
    st.write("1. Enjoy the beautiful sunrise safely.")
    st.write("2. If you're outside, be cautious of morning dew, it can make surfaces slippery.")
    st.write("3. Be mindful of early morning traffic if you're on the road.")
