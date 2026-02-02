import torch
from ultralytics import YOLO
from ultralytics.nn.tasks import DetectionModel
import cv2
import matplotlib.pyplot as plt

# Allowlist the DetectionModel for safe loading
torch.serialization.add_safe_globals([DetectionModel])

def main():
    # Load YOLOv8 model
    model = YOLO("best.pt")

    # Load sample image
    img_path = "demo/sample_image.jpg"
    img = cv2.imread(img_path)
    if img is None:
        print("Sample image not found. Please add a sample X-ray image to demo/sample_image.jpg")
        return

    # Run inference
    results = model(img)

    # Plot results
    output_img = results[0].plot()

    # Display using matplotlib
    plt.imshow(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
    plt.title("Threat Detection Results")
    plt.axis('off')
    plt.show()

    # Print detections
    for result in results:
        for box in result.boxes:
            cls = int(box.cls[0])
            conf = box.conf[0]
            class_name = model.names[cls]
            print(f"Detected: {class_name} with confidence {conf:.2f}")

if __name__ == "__main__":
    main()