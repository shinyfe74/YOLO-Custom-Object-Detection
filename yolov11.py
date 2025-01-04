from ultralytics import YOLO
model = YOLO("yolo11x.pt")  # load an official model
### yolo11n.pt yolo11s.pt yolo11m.pt yolo11l.pt yolo11x.pt

Train_result = model.train(data="custom_data.yaml", epochs=100, batch=16, plots = True, time=True, save=True)

