#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Part2:
Loads one frame of a movie and puts it together with an instance of continuous
rating and writes out a png image per frame.
"""
from __future__ import division
import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import cv2

root = 'path/to/root/folder/'
os.chdir(root)
# here I am loading some real data traces to put together with the video frame
if myhost == 'PCX0049':
    file_dir = 'path/to/data'
    savepath = root

data = np.load(file_dir)
cdt = data['cData_ses1']
# rating data curve
cr = cdt[16, 1, :] * -1
# tho get number of frames and frames per sec
video_cap = cv2.VideoCapture('video.mp4')
nr_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video_cap.get(cv2.CAP_PROP_FPS)

############### place the video and rating together on a subplot ###############
sns.set_style('white')
sns.set_context('talk')
# repeat every value 3 times so that rating curve matches with the number of
# movie frames
plot_ind = np.repeat(np.arange(1, 301), 3)
for i in range(1, nr_frames - 4): # i want 900 frames
    fig, ax = plt.subplots(2, 1, figsize=(7, 10))
    sns.despine()
    # load video frame and display on the first axis
    image_file = 'frames_from_video/frame_' + str(i) + '.png'
    image = plt.imread(image_file)
    ax[0].imshow(image)
    ax[0].axis('off')
    ax[1].set_ylim(-1.2, 1.2)
    ax[1].set_xlim(0, 300)

    k = plot_ind[i-1]
    ax[1].plot(cr[:k], '-', color = 'green', lw=3)
    ax[1].set_xlabel('Duration (sec)')
    ax[1].set_ylabel('Rating')
    ax[1].set_xticklabels(np.arange(0, 32, 5))

    # save the image
    fname =  savepath + 'frame_' + '%.3d' %i + '.png'
    plt.savefig(fname, dpi=90)
    plt.close()
