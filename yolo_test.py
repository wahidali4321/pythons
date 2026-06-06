from ultralytics import YOLO

model = YOLO("yolov8n.pt")   # pretrained model
results = model("C:\Users\wahid\Documents\GitHub\python\wahid.jpg") # run detection
results.show()