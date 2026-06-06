from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # pretrained model
results = model("image.jpg") # run detection
results.show()