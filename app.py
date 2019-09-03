#from flask import Flask
from keras.models import load_model
from keras.applications.resnet50 import ResNet50

# coding=utf-8
import sys
import os
import glob
import re
import numpy as np

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer


app = Flask(__name__)

MODEL_PATH='models/your_model.h5'

model = ResNet50(weights='imagenet')
print('Model loaded')



def model_predict(img_path, model):
 
 	img=image.load_img(img_path, target_size=(224,224))

 	x=image.img_to_array(img)

 	#x=np.expand_dims(x,axis=0)

 	#x=preprocess_input(x,mode='caffe')

 	preds= model.predict(x)

 	return preds



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def upload():
    if request.method == 'POST':

    	f=request.files['file']

    	f.save(file_path)

    	preds= model_predict(file_path, model)

    	pred_class=decode_predictions(preds, top=1)

    	return pred_class