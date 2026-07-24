import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import pandas as pd
from collections import Counter

# Load YOLO Model
model = YOLO("yolov8n.pt")

# Title
st.title("YOLO Detection")

# Upload Image
file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png", "webp"]
)

if file:

    # Open Image
    image = Image.open(file)

    # Run YOLO
    results = model(np.array(image))

    # Draw Bounding Boxes
    result = results[0].plot()

    # Show Image
    st.image(result, caption="Detection Result", use_container_width=True)

    # Get Class Names
    names = model.names

    # Get Detected Classes
    classes = results[0].boxes.cls.tolist()

    # Convert IDs to Names
    labels = [names[int(i)] for i in classes]

    # Count Objects
    counts = Counter(labels)

    st.subheader("Detection Summary")

    if len(counts) == 0:
        st.write("No objects detected.")
    else:
        df = pd.DataFrame({
            "Object": list(counts.keys()),
            "Count": list(counts.values())
        })

        st.table(df)
