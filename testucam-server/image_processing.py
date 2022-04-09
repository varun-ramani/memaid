import cv2
import numpy as np

def handle_yuv420(height, width, plane1, plane2, plane3):
    plane1_arr = np.frombuffer(plane1, dtype=np.uint8)
    plane2_arr = np.frombuffer(plane2, dtype=np.uint8)
    plane3_arr = np.frombuffer(plane3, dtype=np.uint8)

    plane1 = np.reshape(plane1_arr, (height, width))
    plane2 = np.reshape(plane2_arr, (height, width))
    plane3 = np.reshape(plane3_arr, (height, width))

    image = np.dstack((plane1, plane2, plane3))

    cv2.imshow('rgb_image', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    cv2.waitKey(1)