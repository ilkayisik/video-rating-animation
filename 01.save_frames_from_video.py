#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part1: saves each frame of a video as an image
"""
import os
import cv2

root = 'path/to/root/folder/'
os.chdir(root)
video_cap = cv2.VideoCapture('video.mp4')
success, image = video_cap.read()
count = 1
while success:
  # save frames as png files
  cv2.imwrite("frames_from_video/frame_%d.png" % count, image)
  success, image = video_cap.read()
  print('Read a new frame: ', success)
  count += 1
