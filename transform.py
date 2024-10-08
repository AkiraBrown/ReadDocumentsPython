import numpy as np
import cv2

def order_points(pts):
    rect = np.zeros((4,2), dtype= "float32")

    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)] #Top left
    rect[2] = pts[np.argmin(s)] #Top Right

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)] # Bottom left
    rect[3] = pts[np.argmin(diff)] # Bottom right

    return rect

def four_point_transform(image,pts):
    rect = order_points(pts)
    (tl,tr,bl,br) = rect # destructure all four points from rect 
    widthA = np.sqrt(((br[0]-bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0]-tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    max_width = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0]-br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0]-bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    max_height = max(int(heightA), int(heightB))

    dst = np.array([[0,0], [max_width - 1, 0], [max_width - 1, max_height - 1], [0,max_height - 1]], dtype= "float32")

    M = cv2.getPerspectiveTransform(rect,dst)
    warped = cv2.warpPerspective(image,M, (max_width,max_height))
    return warped

