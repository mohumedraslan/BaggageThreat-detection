# Baggage Threat Detection Using X-Ray

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## ML-powered threat detection in X-ray images for baggage screening, with automated MLOps pipelines.

## Overview
This project builds an MLOps pipeline for baggage threat detection using the SixRay dataset. It automates training, validation, and deployment of a YOLOv8 model, achieving high accuracy and low inference latency. The pipeline uses CI/CD, FastAPI for model serving, and Streamlit for interactive deployment, ensuring scalability for real-time security applications.

🔗 Live Demo: [Baggage Threat Detection App](https://moraslan-baggage-threat-detection.streamlit.app/)

## Features
- **Threat Detection**: YOLOv8 model to detect and classify threats in X-ray images.
- **MLOps Automation**: CI/CD with GitHub Actions, reducing deployment time.
- **Real-Time Inference**: FastAPI endpoint with low inference latency.
- **Interactive UI**: Deployed on Streamlit Cloud for user-friendly inference.
- **Optimized Preprocessing**: OpenCV for efficient image processing.

## Tech Stack
- **ML**: PyTorch, YOLOv8, OpenCV
- **MLOps**: GitHub Actions (CI/CD), FastAPI, Streamlit
- **Programming**: Python
- **Data**: Pandas, NumPy
- **Version Control**: Git, GitHub

## Project Structure
```
BaggageThreat-detection/
├── app.py              # Streamlit app for threat detection
├── best.pt             # Pre-trained YOLOv8 model weights
├── requirements.txt    # Dependencies
├── demo/               # Demo files
│   ├── sample_image.jpg
│   └── demo.py
├── .gitignore          # Git ignore file
├── LICENSE             # MIT License
└── README.md           # Documentation
```

## Installation and Setup
### Prerequisites
- Python 3.8+
- Git

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mohumedraslan/BaggageThreat-detection.git
   cd BaggageThreat-detection
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App Locally**:
   ```bash
   streamlit run app.py
   ```
   Open http://localhost:8501 in your browser to use the app.

## Usage
- Launch the app via the live demo or locally.
- Upload an X-ray image (PNG/JPEG).
- View the threat detection results with bounding boxes and confidence scores.

## Demo
To run a quick demo with a sample image:
1. Add a sample X-ray image named `sample_image.jpg` to the `demo/` folder.
2. Run:
   ```bash
   python demo/demo.py
   ```
This will process the sample X-ray image and display the detection results.

## MLOps Workflow
- **CI/CD**: GitHub Actions automates testing, training, and deployment.
- **Training**: YOLOv8 model on SixRay dataset.
- **Deployment**: FastAPI for inference, hosted on Streamlit Cloud.
- **Preprocessing**: OpenCV for real-time inference.

## Results
- High accuracy on SixRay test set.
- Low latency for real-time use.
- Efficient CI/CD pipeline.

## Contributing
Fork the repo, create a branch, and submit a pull request. Open an issue for major changes.

## License
This project is licensed under the MIT License.

## Contact
- **Author**: Mohamed Raslan
- **Email**: mohamedraslan@gmail.com
- **LinkedIn**: [Mohamed Raslan](https://www.linkedin.com/in/mohumed-raslan/)
- **GitHub**: [mohumedraslan](https://github.com/mohumedraslan)
