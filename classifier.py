import tensorflow as tf
import keras
import os
import cv2
from PIL import Image
import imghdr
import numpy as np
from matplotlib import pyplot as plt

Image.open

data_dir = 'data'

image_exts = ['jpeg', 'jpg', 'bmp',  'png']

# print(os.listdir(os.path.join(data_dir, 'happy')))

# print(cv2.imread(os.path.join('data', 'happy', 'bigstock_Happy_Business_People_With_Han_4049346.jpg')))

for image_class in os.listdir(data_dir):
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try:
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts:
                print('Image not in ext list {}'.format(image_path))
                os.remove(image_path)
        except Exception as e:
            print('Issue with image {}'.format(image_path))


data = keras.utils.image_dataset_from_directory('data')
data_iterator = data.as_numpy_iterator()
batch = data_iterator.next()
print(batch)
