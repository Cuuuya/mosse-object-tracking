import os
import cv2
import imageio

def get_img(img_path):
    frame_list = []
    for frame in os.listdir(img_path):
        if os.path.splitext(frame)[1] == '.jpg':
            frame_list.append(os.path.join(img_path, frame))
    return frame_list

def create_gif(image_list, gif_name):
    frames = []
    for i in image_list:
        frames.append(imageio.imread(i))
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.05)
    return

path = 'record_frames/surfer/'
list = get_img(path)
create_gif(list, 'test.gif')