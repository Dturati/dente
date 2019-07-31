import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('davi.JPG')

# type(img_raw)
# cv2.imshow("teste.png",img_raw)
# img = cv2.cvtColor(img_raw,cv2.COLOR_BGR2RGB)
# cv2.imwrite('teste.png',img)
while True:
    cv2.imshow('davi',img)
    image_black = np.zeros(shape=(512,512,3),dtype=np.int16)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.imwrite('teste.png',image_black)
cv2.imwrite('teste2.png',image_black)
cv2.destroyAllWindows()