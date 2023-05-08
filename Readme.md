### HELMET DETECTION OF RIDER
##INSTALL REQUIREMENTS 

pip install -r requirements.txt

##TRAIN MODEL 

python train.py --name NAME_OF_MODEL --batch-size 2 --epochs 60 --cfg ./models/yolov5l.yaml --weights ./yolov5l.pt --data ./PATH_TO_data.yaml/  


#ARGS
 --img-size :- size of image if all images are same size (improves accuracy)
 --device :- cuda device, i.e. 0 or 0,1,2,3 or cpu
 --batch-size : iamges per batch as per gpu and system memory (higher reduce time per epoch)
 --epochs : training epochs (higher improves accuracy but sometimes overfit)
 --cfg :- model configuration; can be yolov5s.yaml, yolov5m.yaml, yolov5l.yaml, yolov5x.yaml
 --weights :- pretrained weights; can be yolov5s.pt, yolov5m.pt, yolov5l.pt, yolov5x.pt
 --data :- path to data.yaml file  


##DETECT 

python detect.py --device 0 --source ./PATH_TO_IMAGES_OR_VIDEO/ --weights ./PATH_TO_TRAINED_MODEL/

#ARGS 
 
  --device :- cuda device, i.e. 0 or 0,1,2,3 or cpu (if detect on gpu generate error then use cpu as argument)
  --weights :- path to trained model
  --source :- path to images or videos
  --img-size :- size of image if all images are same size (improves accuracy)
  --conf :- minimum confidence to detect object


##TENSORBOARD 

tensorboard --logdir runs/train 

# run above command in command prompt in same directory and then paste http://localhost:6006/  in any browser
