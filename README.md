# Python-Video-Editor-
A simple script that edits your video clips randomly

# Usage
Make sure to install moviepy first
```
pip install moviepy
```

You need to provide three arguments for the script
to work properly. The path for the video files,
start and stop seconds to cut from each video clip.

example:
```
python video_edit.py /home/user/Desktop/Videos/ 0 5
```
in this example the script will cut 5 seconds from each clip and 
then concatenate them to create an output mp4 file.
