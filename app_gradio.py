# app_gradio.py
import gradio as gr
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = load_model("Blood Cell.h5")
class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']

def predict(img):
    img = cv2.resize(img, (224, 224))
    img = preprocess_input(np.expand_dims(img, axis=0))
    prediction = model.predict(img)
    label = class_labels[np.argmax(prediction)]
    return label

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload Blood Cell Image"),
    outputs=gr.Label(label="Predicted Cell Type"),
    title="HematoVision - Blood Cell Classifier"
)

interface.launch()
