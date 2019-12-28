# -*- coding: utf-8 -*-
# @Author: Atish Agrawal
# @Date:   2019-12-28 12:58:15
# @Last Modified by:   Atish Agrawal
# @Last Modified time: 2019-12-28 13:13:48

import cv2
import time
import os
from glob import glob
from tkinter import filedialog
from tkinter import *
from pathlib import Path


def video_to_frames(input_loc):
    # Log the time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n" + os.path.basename(input_loc))
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        if count == video_length - 1:
	        cv2.imwrite(
	            os.path.dirname(input_loc) + "/" + os.path.basename(os.path.splitext(input_loc)[0]) + str(count)+"_shot.jpg",
	            frame)
        count = count + 1
        # If there are no more frames left
        if count > (video_length - 1):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print("It took %d seconds for conversion." % (time_end - time_start))
            break


def searchMp4Files(start_dir):
    files = []
    pattern = "**/*.mp4"

    for filename in Path(start_dir).glob(pattern):
        files.append(str(filename.resolve()))

    print("Found: " + str(files.__len__()) + " files.")

    # Iterate over all mp4 Files and extract the video Frames
    for individual_video in files:
        video_to_frames(individual_video)

    pass


def showDirectoryChooser():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()

    return folder_selected

    pass


if __name__ == "__main__":
    # Search for all mp4 Files

    searchMp4Files(showDirectoryChooser())
