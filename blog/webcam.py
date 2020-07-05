# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:01:39 2020

@author: Legedith
"""


import cv2
from threading import Thread
   
class Webcam:
   
    def __init__(self):
        # self.video_capture = cv2.VideoCapture(0)
        self.video_capture = cv2.VideoCapture('http://192.168.43.1:8080/video')
        self.current_frame = self.video_capture.read()[1]
           
    # create thread for capturing images
    def start(self):
        Thread(target=self._update_frame, args=()).start()
   
    def _update_frame(self):
        while(True):
            self.current_frame = self.video_capture.read()[1]
                   
    # get the current frame
    def get_current_frame(self):
        return self.current_frame