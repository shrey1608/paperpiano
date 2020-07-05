# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 21:01:16 2020

@author: Legedith
"""


import cv2
import numpy as np
 
class Detection(object):
 
    THRESHOLD = 500
 
    def __init__(self, image):
        self.previous_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
    def get_active_cell(self, image):
        # obtain motion between previous and current image
        current_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        delta = cv2.absdiff(self.previous_gray, current_gray)
        threshold_image = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('frame',threshold_image)
        # debug
        # cv2.imshow('OpenCV Detection', image)
        cv2.waitKey(10)
 
        # store current image
        self.previous_gray = current_gray
 
        # set cell width
        height, width = threshold_image.shape[:2]
        cell_width = width//8
 
        # store motion level for each cell
        cells = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        start = height//3
        end = height//2 +30
        cells[0] = cv2.countNonZero(threshold_image[start:end, 0:cell_width])
        cells[1] = cv2.countNonZero(threshold_image[start:end, cell_width:cell_width*2])
        cells[2] = cv2.countNonZero(threshold_image[start:end, cell_width*2:cell_width*3])
        cells[3] = cv2.countNonZero(threshold_image[start:end, cell_width*3:cell_width*4])
        cells[4] = cv2.countNonZero(threshold_image[start:end, cell_width*4:cell_width*5])
        cells[5] = cv2.countNonZero(threshold_image[start:end, cell_width*5:cell_width*6])
        cells[6] = cv2.countNonZero(threshold_image[start:end, cell_width*6:cell_width*7])
        cells[7] = cv2.countNonZero(threshold_image[start:end, cell_width*7:width])
 
        # obtain the most active cell
        top_cell =  np.argmax(cells)
        imagec = threshold_image.copy()
        imagec = cv2.line(imagec, (cell_width,start), (cell_width,end), (70, 255, 70), 5)
        imagec = cv2.line(imagec, (cell_width*2,start), (cell_width*2,end), (70, 255, 70), 5) 
        imagec = cv2.line(imagec, (cell_width*3,start), (cell_width*3,end), (70, 255, 70), 5) 
        imagec = cv2.line(imagec, (cell_width*4,start), (cell_width*4,end), (70, 255, 70), 5) 
        imagec = cv2.line(imagec, (cell_width*5,start), (cell_width*5,end), (70, 255, 70), 5) 
        imagec = cv2.line(imagec, (cell_width*6,start), (cell_width*6,end), (70, 255, 70), 5) 
        imagec = cv2.line(imagec, (cell_width*7,start), (cell_width*7,end), (70, 255, 70), 5) 


        # return the most active cell, if threshold met
        if(cells[top_cell] >= self.THRESHOLD):
            cv2.putText(image,'*',(height//2, cell_width*top_cell), cv2.FONT_HERSHEY_SIMPLEX, 4,(255,255,255),2)
            cv2.imshow('OpenCV Detection', image)
            cv2.imshow('border', imagec)
            return top_cell
        else:
            cv2.imshow('OpenCV Detection', image)
            cv2.imshow('border', imagec)
            return None