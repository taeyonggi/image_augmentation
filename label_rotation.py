import cv2
import numpy as np


def rotate_box(bb, cx, cy, h, w, angle):
    """
    Rotate bounding box.
    """

    new_bb = list(bb)
    new_bb[1] = float(new_bb[1]) * w
    new_bb[2] = float(new_bb[2]) * h

    # Translate box so that center is at origin
    new_bb[1] -= cx
    new_bb[2] -= cy

    radians = angle * np.pi / 180
    # Apply rotation matrix
    rot_mat = np.array([[np.cos(radians), np.sin(radians)], [-np.sin(radians), np.cos(radians)]])
    new_bb[1], new_bb[2] = rot_mat.dot([new_bb[1], new_bb[2]])

    if (angle == 90) or (angle == 270):
        new_bb[3] = float(bb[4])
        new_bb[4] = float(bb[3])
        new_bb[1] += cy
        new_bb[2] += cx
        new_bb[1] = float(new_bb[1]) / h
        new_bb[2] = float(new_bb[2]) / w
    else:
        new_bb[4] = float(new_bb[4]) # /n 지우기
        new_bb[1] += cx
        new_bb[2] += cy
        new_bb[1] = float(new_bb[1]) / w
        new_bb[2] = float(new_bb[2]) / h
    # Translate box back to original position

    new_bb[1] = str(new_bb[1])
    new_bb[2] = str(new_bb[2])
    new_bb[3] = str(new_bb[3])
    new_bb[4] = str(new_bb[4])
    return new_bb

def flip_yolo_LR(bb, img_width):
    """
    Flip YOLO bounding box coordinates horizontally.
    """
    new_bb = list(bb)
    x_center = float(bb[1]) * img_width
    new_x_center = img_width - x_center
    new_bb[1] = new_x_center / img_width
    new_bb[1] = str(new_bb[1])
    new_bb[4] = float(new_bb[4]) # /n 지우기
    new_bb[4] = str(new_bb[4])
    return new_bb

def flip_yolo_TB(bb, img_height):
    """
    Flip YOLO bounding box coordinates vertically.
    """
    new_bb = list(bb)
    y_center = float(bb[2]) * img_height
    new_y_center = img_height - y_center
    new_bb[2] = new_y_center / img_height
    new_bb[2] = str(new_bb[2])
    new_bb[4] = float(new_bb[4]) # /n 지우기
    new_bb[4] = str(new_bb[4])
    return new_bb

for i in range(1, 1633):
    img = cv2.imread('train (' + str(i) +').jpg')
    h, w = img.shape[:2]
    cx = w / 2
    cy = h / 2

    f = open("train (" + str(i) +").txt", 'r')
    f1 = open("train (" + str(i) +")_90.txt", 'w')
    f2 = open("train (" + str(i) +")_180.txt", 'w')
    f3 = open("train (" + str(i) +")_270.txt", 'w')
    f4 = open("train (" + str(i) +")_LR.txt", 'w')
    f5 = open("train (" + str(i) +")_TB.txt", 'w')
    lines = f.readlines()
    for line in lines:
        line = line.split(" ")
        list_90 = rotate_box(line, cx, cy, h, w, 90)
        list_180 = rotate_box(line, cx, cy, h, w, 180)
        list_270 = rotate_box(line, cx, cy, h, w, 270)
        list_LR = flip_yolo_LR(line, w)
        list_TB = flip_yolo_TB(line, h)
        for z in list_90:
            f1.write(z)
            f1.write(" ")
        f1.write("\n")
        for z in list_180:
            f2.write(z)
            f2.write(" ")
        f2.write("\n")
        for z in list_270:
            f3.write(z)
            f3.write(" ")
        f3.write("\n")
        for z in list_LR:
            f4.write(z)
            f4.write(" ")
        f4.write("\n")
        for z in list_TB:
            f5.write(z)
            f5.write(" ")
        f5.write("\n")
    f5.close()
    f4.close()
    f3.close()
    f2.close()
    f1.close()
    f.close()









