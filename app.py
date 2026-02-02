import streamlit as st
import torch
from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
import cv2
import numpy as np
from PIL import Image

# Allowlist the DetectionModel for safe loading
torch.serialization.add_safe_globals([DetectionModel])

st.title("Baggage Threat Detection System")
st.write("Upload an X-ray image to detect potential threats using YOLOv8.")

# Load YOLOv8 model
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# File uploader for images
uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
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

    # Display detection details
    st.subheader("Detection Details")
    if results[0].boxes:
        for i, box in enumerate(results[0].boxes):
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            class_name = model.names[cls]
            x1, y1, x2, y2 = box.xyxy[0]
            st.write(f"**Detection {i+1}:** {class_name} (Confidence: {conf:.2f}) at [{x1:.0f}, {y1:.0f}, {x2:.0f}, {y2:.0f}]")
    else:
        st.write("No threats detected.")

st.markdown("---")
st.write("**Note:** This is a demo application. For production use, ensure proper security measures.")
