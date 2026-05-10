import cv2
import os
import time
import sys
import threading
import pygame
from PIL import Image
os.system("")
ascii_chars = " .:-=+*#%@"

video_path = "bad apple.mp4"
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("bad apple.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

music_thread = threading.Thread(target=play_music,daemon=True)
music_thread.start()
# 然後開始播 ASCII 動畫
with open("ascii_frames.txt", "r", encoding="utf-8") as f:
    content = f.read()

frames = content.split("===FRAME===")

frame_time = 1 / fps
start_time=time.time()

print("\033[2J")  # 清空一次

for i,frame in enumerate(frames):
    target_time = start_time + i * frame_time

    sys.stdout.write("\033[H" + frame)
    sys.stdout.flush()

    now = time.time()
    sleep_time = target_time - now
    if sleep_time > 0:
        time.sleep(sleep_time)
