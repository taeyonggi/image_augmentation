import numpy as np
from matplotlib.pyplot import imshow, subplots, title
from PIL import Image
from torchvision import transforms
import albumentations
import random
import cv2
import matplotlib.pyplot as plt

for i in range(1,205):
    img = Image.open('train ('+str(i)+').jpg')

    loader_transform1 = transforms.ColorJitter(brightness=3)
    loader_transform2 = transforms.ColorJitter(contrast=2)
    loader_transform3 = transforms.ColorJitter(saturation=2)
    loader_transform4 = transforms.ColorJitter(hue=0.3)

    img_aug1 = loader_transform1(img)
    img_aug2 = loader_transform2(img)
    img_aug3 = loader_transform3(img)
    img_aug4 = loader_transform4(img)

    img_aug1.save('train ('+str(i)+'-1).jpg', "JPEG")
    img_aug2.save('train ('+str(i)+'-2).jpg', "JPEG")
    img_aug3.save('train ('+str(i)+'-3).jpg', "JPEG")
    img_aug4.save('train ('+str(i)+'-4).jpg', "JPEG")

    for j in range(5,8):
        imgArray_aug = np.array(Image.open('train ('+str(i)+').jpg'))

        indx1 = random.sample(range(400), 2)
        indx2 = random.sample(range(400), 2)

        length = (np.max(indx1) - np.min(indx1)) * (np.max(indx2) - np.min(indx2)) * 3

        imgArray_aug[np.min(indx1):np.max(indx1), np.min(indx2):np.max(indx2), range(3)] = np.random.choice(256, length, replace=True).reshape(
                ((np.max(indx1) - np.min(indx1)), (np.max(indx2) - np.min(indx2)), 3))
        Image.fromarray(imgArray_aug).save('train ('+str(i)+'-'+str(j)+').jpg', "JPEG")