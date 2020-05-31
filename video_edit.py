from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip as cut_video
from moviepy.editor import VideoFileClip, concatenate_videoclips
from time import sleep
import os, sys


vid_path = sys.argv[1]
start_sec = sys.argv[2]
stop_sec = sys.argv[3]

# Function to rename mp4 files according to count ex: video0.mp4...
def rename(): 

    for count, filename in enumerate(os.listdir(vid_path)): 
        dst = "video" + str(count) + ".mp4"
        src = vid_path + filename
        dst = vid_path + dst

        # rename all the files 
        os.rename(src, dst)
  

# Cut videos according to start and stop arguments 
def cut():
    for count, filename in enumerate(os.listdir(vid_path)):
        cut_video(vid_path + 'video' + str(count) + '.mp4', int(start_sec), int(stop_sec), targetname=vid_path + str(count) + '.mp4')


# Create the final video by joining the clips
def concat():

    # In this example I have 5 clips you can create more variables for more clips     
    clip1 = VideoFileClip(vid_path + '0.mp4')
    clip2 = VideoFileClip(vid_path + '1.mp4')
    clip3 = VideoFileClip(vid_path + '2.mp4')
    clip4 = VideoFileClip(vid_path + '3.mp4')
    clip5 = VideoFileClip(vid_path + '4.mp4')

    # Pass in all the clips that you want to join, you can play with the order
    final_clip = concatenate_videoclips([clip2, clip1, clip3, clip4, clip5])
    # Create the output file in the same directory
    final_clip.write_videofile(vid_path + 'output.mp4')

# call the functions synchronously 
rename()  
cut()
concat()
                       
