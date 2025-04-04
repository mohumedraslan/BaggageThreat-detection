import streamlit as st
import torch
from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel

# Allowlist the DetectionModel for safe loading
torch.serialization.add_safe_globals([DetectionModel])

st.title("Baggage Threat Detection System")
st.write("Upload an image to detect potential threats.")

# Load YOLOv8 model
model = YOLO("best.pt")

# File uploader for images
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    from PIL import Image
    import cv2
    import numpy as np
    
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert to OpenCV format
    img_array = np.array(image)
    img_cv2 = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    
    # Run YOLOv8 inference
    results = model(img_cv2)
    output_img = results[0].plot()
    
    # Convert back to RGB and display
    output_img_rgb = cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB)
    st.image(output_img_rgb, caption="Detection Result", use_column_width=True)
