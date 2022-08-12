import cv2
import numpy as np
import random
import os

from PIL import image
import time
import imutils
from tensorflow.keras.models import load_model
os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
net = cv2.dnn.readnet("yolo3-custom_7000.weights", "yolo3-custom.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)
model = load_model('helmet-nonhelmet_cnn.h5')
print('model loaded!!!!')
cap = cv2.VideoCapture('testing video/test2.mp4')
COLORS = [(0,255,0),(0,0,255)]

def helmet_or_nohelmet(helmet_roi):

    try:
        helmet_roi = cv2.resize(helmet_roi, (224, 224))
        helmet_roi = np.array(helmet_roi,dtype='float32')
        helmet_roi = helmet_roi.reshape(1, 224, 224, 3)
        helmet_roi = helmet_roi/255.0
        return int(model.predict(helmet_roi)[0][0])
    except:
        pass

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutlayers()]

    ret = True


    while ret:

        ret, img = cap.read()
        img = imutils.resize(img,height=500)
