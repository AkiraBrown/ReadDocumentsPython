import numpy as np
import cv2

def order_points(pts):
    rect = np.zeros((4,2), dtype= "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)] #Top left
    rect[2] = pts[np.argmin(s)] #Top Right

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmin(diff)]

    return rect
