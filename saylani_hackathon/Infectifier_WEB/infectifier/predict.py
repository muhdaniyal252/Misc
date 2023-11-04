import cv2
# import tensorflow as tf
import numpy as np
import pickle

# model = tf.keras.models.load_model('H:/working/saylani/infectifier_AI/classifier.h5')
# img_size = 512
# input_shape = (1,img_size, img_size, 1)

def make_prediction(path):
    import random
    return random.choice([ 'Infected','Not infection'])

    # img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    # img = cv2.resize(img,(img_size,img_size))
    # img = img.reshape(*input_shape)
    # img = img/255
    # pred = model.predict(img)
    # return \
    #     'Really Sorry to inform you that the uploaded X-Ray has infection in chest :(' \
    #         if pred[0][0]>0.5 else \
    #     'No infection identified in uploaded X-Ray image :D'