#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:30:52 2018
@author: ilkay.isik
"""
import cv2
import os

root = 'path/to/root/folder/'
os.chdir(root)
image_folder = 'frames_video_and_rating'
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# tho get number of frames and frames per sec
video_cap = cv2.VideoCapture('video.mp4')
nr_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video_cap.get(cv2.CAP_PROP_FPS)

out_vid = 'video_and_rating_animation.mp4'

# load one image to get the size
frame = os.path.join(image_folder, images[1])
img = cv2.imread(frame)
height, width, layers = img.shape
size = (width, height)

frame_array = []
files = [img for img in os.listdir(image_folder) if img.endswith(".png")]


for i in range(len(files)):
    filename = os.path.join(image_folder, files[i])
    img = cv2.imread(filename)
    # inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(out_vid, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
