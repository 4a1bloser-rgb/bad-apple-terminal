import os
import time
import sys
import threading
from urllib.request import urlopen
from urllib.request import urlretrieve

os.system("")

ascii_chars = " .:-=+*#%@"

# 直接手動設定 FPS（因為不用 cv2 讀影片了）
fps = 30
frame_time = 1 / fps

mp3_url="https://raw.githubusercontent.com/4a1bloser-rgb/bad-apple-terminal/main/bad_apple.mp3"

def play_music(): 
    urlretrieve(mp3_url, "bad_apple.mp3")
    print("mp3 exists:", os.path.exists("bad_apple.mp3"))
    os.system('start "" "bad_apple.mp3"')
music_thread = threading.Thread( target=play_music, daemon=True )
music_thread.start()

# GitHub Raw 的 ASCII txt 網址
url = "https://raw.githubusercontent.com/4a1bloser-rgb/bad-apple-terminal/main/ascii_frames.txt"

# 用標準函式庫 urllib 抓文字
text = urlopen(url).read().decode("utf-8")

# 分割每一幀
frames = text.split("===FRAME===")

start_time = time.time()

print("\033[2J")  # 清空一次畫面

for i, frame in enumerate(frames):
    target_time = start_time + i * frame_time

    # 回到左上角覆蓋畫面
    sys.stdout.write("\033[H" + frame)
    sys.stdout.flush()

    now = time.time()
    sleep_time = target_time - now

    if sleep_time > 0:
        time.sleep(sleep_time)
