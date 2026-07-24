
# YOLO Object Detection using Streamlit

A simple web application built with **Streamlit** and **YOLOv8 (Ultralytics)** that performs real-time object detection on uploaded images.

## 📌 Project Description

This application allows users to upload an image, detect objects using a pre-trained YOLOv8 model, display bounding boxes around detected objects, and generate a summary showing the number of detected objects for each class.

## ✨ Features

- Upload images (JPG, JPEG, PNG, WEBP)
- Detect multiple objects using YOLOv8
- Draw bounding boxes on detected objects
- Display detection results
- Count detected objects by class
- Show detection summary in a table

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run app.py
```

4. Open the Streamlit link in your browser and upload an image.

## 🛠️ Technologies Used

- Python
- Streamlit
- Ultralytics YOLOv8
- NumPy
- Pandas
- Pillow

## 📂 Project Structure

```
YOLO_Object_Detection/
│── app.py
│── yolov8n.pt
│── requirements.txt
└── README.md
```

## 📊 Output

The application displays:
- The uploaded image with detected objects highlighted using bounding boxes.
- A detection summary table showing the object names and the number of detected instances.

Example:

| Object | Count |
|--------|------:|
| Person | 5 |
| Car | 3 |
| Dog | 1 |

## 👩‍💻 Author

**Basmala Taha**
