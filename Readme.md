# Helmet Detection and License Plate Extraction using YOLOv5
This project is designed to detect if a rider is wearing a helmet and extract the license plate number of the bike if the rider is not wearing a helmet. The project uses YOLOv5 deep learning algorithm for object detection.
## How it Works
The project uses computer vision techniques to detect the presence of a helmet on a rider's head and the license plate on the bike. The YOLOv5 model is trained on a dataset of images that contain different types of helmets and license plates.<br/>
When an image is fed into the model, it scans the image and identifies any helmets or license plates that are present in the image. If the model detects that the rider is not wearing a helmet, it will extract the license plate number and store it in a file.


## Installation
git clone https://github.com/username/helmet-license-plate-detection.git<br/>
pip install -r requirements.txt

## TRAIN MODEL 
python train.py --name NAME_OF_MODEL --batch-size 16 --epochs 300 --cfg ./models/yolov5l.yaml --weights ./yolov5l.pt --data ./PATH_TO_data.yaml/  
### ARGS
 --img-size :- size of image if all images are same size (improves accuracy)<br/>
 --device :- cuda device, i.e. 0 or 0,1,2,3 or cpu<br/>
 --batch-size : iamges per batch as per gpu and system memory (higher reduce time per epoch)<br/>
 --epochs : training epochs (higher improves accuracy but sometimes overfit)<br/>
 --cfg :- model configuration; can be yolov5s.yaml, yolov5m.yaml, yolov5l.yaml, yolov5x.yaml<br/>
 --weights :- pretrained weights; can be yolov5s.pt, yolov5m.pt, yolov5l.pt, yolov5x.pt<br/>
 --data :- path to data.yaml file  <br/>
 --autoanchor : to automatically resize the image<br/>

## DETECT 
python detect.py --device 0 --source ./PATH_TO_IMAGES_OR_VIDEO/ --weights ./PATH_TO_TRAINED_MODEL/
### ARGS 
 
  --device :- cuda device, i.e. 0 or 0,1,2,3 or cpu (if detect on gpu generate error then use cpu as argument)<br/>
  --weights :- path to trained model<br/>
  --source :- path to images or videos<br/>
  --img-size :- size of image if all images are same size (improves accuracy)<br/>
  --conf :- minimum confidence to detect object<br/>

