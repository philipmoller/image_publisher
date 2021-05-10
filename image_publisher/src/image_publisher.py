#!/usr/bin/env python2.7

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import os
import numpy as np

def img_publisher(image, publisher):
    bridge = CvBridge()
    imgMsg = bridge.cv2_to_imgmsg(image, "bgr8")

    publisher.publish(imgMsg)



if __name__ == '__main__':
    rospy.init_node('image_publisher')
    pub = rospy.Publisher('image', Image, queue_size=1)

    while 1:
        for i in range(246,269):
            print(i)
            img_name = "test_set/reduced_sidewalk{}.png".format(i)
            print(img_name)
            img = cv2.imread(img_name)
            try:
                img_publisher(img, pub)
                rospy.sleep(0.3)
            except rospy.ROSInterruptException:
                pass
