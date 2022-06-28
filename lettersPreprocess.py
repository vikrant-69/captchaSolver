import csv
from PIL import Image
import numpy as np
import string
import os

file_path = "D:\Project\Mosaic\dataset\csv_data.csv"

image_Folder_Path = "D:\Project\Mosaic"

Alphabet_Mapping_List = list(string.ascii_uppercase)

for alphabet in Alphabet_Mapping_List:
    path = image_Folder_Path + '\\' + alphabet
    if not os.path.exists(path):
        os.makedirs(path)

with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in reader:
        idx = row.pop(0)

        img_array = np.asarray(row)
        
        img_array = img_array.reshape(28, 28)
        print(img_array.shape)

        break
        # print(img_array)
        new_image = Image.fromarray(img_array.astype('uint8'))

        last_digit_Name = str(Alphabet_Mapping_List[(int)(idx)])
        
        print ("count: ", count)
        print ("Prcessing Alphabet - " + str (last_digit_Name))
        
        image_Path = image_Folder_Path + '\\' + last_digit_Name + '\\' + str(last_digit_Name) + '-' + str(count) + '.png'
        new_image.save(image_Path)
        count = count + 1

        
