import numpy as np
import cv2
import matplotlib.pyplot as plt
import os

def processa1():
    test_image = cv2.imread('media/image/foto6.jpg')
    test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('media/image/fotoSmoke.jpg',test_image_gray)

    def convertToRGB(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    haar_cascade_smile = cv2.CascadeClassifier('processa/data/haarcascade/cascadefina.xml')

    smile_rects = haar_cascade_smile.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5)

    print('Smile found: ', len(smile_rects))

    for (x,y,w,h) in smile_rects:
         cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    img_rgb = convertToRGB(test_image)

    cv2.imwrite('media/image/imgRgb.jpg',img_rgb)


