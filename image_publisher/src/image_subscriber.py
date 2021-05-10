#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
import numpy as np

current_frame = None

def image_callback(data):
    current_frame = np.frombuffer(data.data, dtype=np.uint8).reshape(data.height, data.width, -1)
    print(current_frame.shape)
    cv2.imshow('img',current_frame)
    cv2.waitKey(1)







if __name__ == '__main__':
    rospy.init_node('image_subscriber', anonymous=True)


    rospy.Subscriber('image', Image, image_callback)

    rospy.spin()
