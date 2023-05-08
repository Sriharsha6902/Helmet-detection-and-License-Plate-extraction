# Helmet Detection and License Plate Extraction using YOLOv5
This project is designed to detect if a rider is wearing a helmet and extract the license plate number of the bike if the rider is not wearing a helmet. The project uses YOLOv5 deep learning algorithm for object detection. The image or video is fed to the model using a user-friendly GUI which then displays the results.
## How it Works
The project uses computer vision techniques to detect the presence of a helmet on a rider's head and the license plate on the bike. The YOLOv5 model is trained on a dataset of images that contain different types of helmets and license plates.<br/>
When an image is fed into the model, it scans the image and identifies any helmets or license plates that are present in the image. If the model detects that the rider is not wearing a helmet, it will extract the license plate number and store it in a file.<br/>
The license plates of the bike will be cropped and saved into two seperate folders "number_plates" and "number_plates_text". The 'number_plates' will contain the images of the number plates while the 'number_plates_text' will contain text file which has the number plate.They are also stored into a csv according to their timestamp so that the user will know when the person didn't wear the helmet.



## Installation
 1. git clone https://github.com/Sriharsha6902/Helmet-detection-and-License-Plate-extraction.git<br/>
 2. pip install -r requirements.txt
 3. train the model using the dataset chosen
 4. integrate it with the GUI
 
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

