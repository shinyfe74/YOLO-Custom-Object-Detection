![sample](https://github.com/AarohiSingla/YOLOv10-Custom-Object-Detection/assets/60029146/d7c1b150-951d-4cab-abff-0e17208da8d6)

### Environment Setup
##### This code is tested on python 3.11

Step -1 :  git clone https://github.com/shinyfe74/YOLO-Custom-Object-Detection.git

Step -2 : Download yolov11 pretrained weights from official repo

Step -3 : Test Pretrained YOLOv11 model using this command: 


##### 1. Inference with pretrained model
```
from ultralytics import YOLO
model = YOLO("yolo11x.pt")  # load an official model
### yolo11n.pt yolo11s.pt yolo11m.pt yolo11l.pt yolo11x.pt
Inferencing_result = model.predict(source="./test_images/1.jpg", conf=0.25, save=True)
```

##### 2. Train Custom model:

1- Custom dataset is required for training the model. Sample dataset is in "custom_dataset" folder, Your dataset should have the same format.

2- Make changes in in custom_data.yaml file as per your dataset

```
model.train(data="custom_data.yaml", epochs=100, batch=16, plots = True, time=True, save=True)
```

##### 3. Load Custom trained model:
```
trained_model = YOLO("runs/detect/train/weights/best.pt")
```
##### 4. Inference with Custom trained model:
```
# image
trained_model.predict(source="./test_images_1/veh2.jpg", conf=0.25, save=True)
#video
trained_model.predict(source="./b.mp4", conf=0.25, save=True)
```
