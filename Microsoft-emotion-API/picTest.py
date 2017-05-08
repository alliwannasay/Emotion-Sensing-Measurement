import types
import numpy as np
from PIL import Image
import os
rule = {'disgust':0,'sadness':1,'neutral':2,'happiness':3,'fear':4,'contempt':5,'surprise':6,'anger':7}
for testLabel in os.listdir(r"./tmp"):
    try:
        label = rule[testLabel]
        for filename in os.listdir(r"./tmp/" + testLabel):
            print("./tmp/"+testLabel+"/"+filename)
    except Exception as e:
        a = 1