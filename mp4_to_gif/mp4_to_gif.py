from moviepy.editor import *
import os

os.mkdir("gif") # the folder which store gif
os.chdir("mp4") # craete a folder, put your mp4 file in this folder
mp4_list = os.listdir()

for i in mp4_list :
    clip = (VideoFileClip(i))
    new_file_name = i.replace("mp4","gif")
    clip.write_gif("../gif/"+new_file_name)
