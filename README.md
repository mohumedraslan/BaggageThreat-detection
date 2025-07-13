# Baggage Threat Detection Using X-Ray


## ML-powered threat detection in X-ray images for baggage screening, with automated MLOps pipelines.

## Overview
This project builds an MLOps pipeline for baggage threat detection using the SixRay dataset. It automates training, validation, and deployment of a TensorFlow model, achieving 95% test accuracy and 200ms inference latency. The pipeline uses CI/CD, FastAPI for model serving, and Streamlit for interactive deployment, ensuring scalability for real-time security applications.

🔗 Live Demo: [Baggage Threat Detection App](https://moraslan-baggage-threat-detection.streamlit.app/)

Features
Threat Detection: TensorFlow model to classify threats in X-ray images.
MLOps Automation: CI/CD with GitHub Actions, reducing deployment time by 2 hours (90% automated).
Real-Time Inference: FastAPI endpoint with inference latency under 200ms.
Interactive UI: Deployed on Streamlit Cloud for user-friendly inference.
Optimized Preprocessing: OpenCV for efficient image processing.
Tech Stack
ML: TensorFlow, OpenCV
MLOps: GitHub Actions (CI/CD), FastAPI, Streamlit
Programming: Python
Data: Pandas, NumPy
Version Control: Git, GitHub
## Project Structure
 ```bash
BaggageThreat-detection/
├── app.py              # Streamlit app for threat detection
├── best.pt             # Pre-trained model weights
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```
Installation and Setup
Prerequisites
Python 3.8+
Git
# Steps
## Clone the Repository:

   ```bash
  git clone https://github.com/mohumedraslan/BaggageThreat-detection.git
  cd BaggageThreat-detection
```
## Install Dependencies:
   ```bash

pip install -r requirements.txt
```
Run the Streamlit App Locally:

   ```bash

streamlit run app.py
Open http://localhost:8501 in your browser to use the app.
```
## Usage
Launch the app via the live demo or locally.
Upload an X-ray image (PNG/JPEG).
View the threat detection results with confidence scores.
MLOps Workflow
CI/CD: GitHub Actions automates testing, training, and deployment.
Training: TensorFlow model on SixRay dataset, 95% accuracy.
Deployment: FastAPI for inference, hosted on Streamlit Cloud.
Preprocessing: OpenCV for real-time inference under 200ms.
Future Plans: Add Kubeflow for orchestration and Prometheus for monitoring.
Results
Accuracy: 95% on SixRay test set.
Latency: Under 200ms for real-time use.
Efficiency: CI/CD cuts deployment time by 2 hours.
Contributing
Fork the repo, create a branch, and submit a pull request. Open an issue for major changes.


Contact
Author: Mohamed Raslan
Email: mohamedraslan@gmail.com
LinkedIn: [Mohamed Raslan](https://www.linkedin.com/in/mohumed-raslan/)
GitHub: [mohumedraslan](https://github.com/mohumedraslan)
