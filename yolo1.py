from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model("wahid.jpg")

results[0].show()