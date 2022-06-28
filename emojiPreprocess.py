import csv
from PIL import Image
import numpy as np
import string
import os
import cv2 




folder_name = ["cloud", "croissant", "heart", "laugh", "smile", "sun"]

for folder in folder_name:
    img_array = os.listdir(f'D:\Project\Mosaic\emojiData\{folder}')
    i=0
    for img_path in img_array:
        emojiPath = f"D:\Project\Mosaic\emojiData\{folder}\{img_path}"

        img = cv2.imread(emojiPath, 1)

        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        (thresh, im_bw) = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        thresh = 250
        im_bw = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY_INV)[1]
        im_bw= cv2.resize(im_bw, (28,28))

        print(f"{folder}-{i}")
        cv2.imwrite(f"D:\Project\Mosaic\{folder}\{folder}-{i}.png", img=im_bw)
        i=i+1

cv2.waitKey(0)
cv2.destroyAllWindows()

