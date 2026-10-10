import ctypes, time
from PIL import ImageGrab

user32 = ctypes.windll.user32
hwnd = 132646

# 激活窗口
user32.ShowWindow(hwnd, 9)  # SW_RESTORE
time.sleep(0.5)
user32.SetForegroundWindow(hwnd)
time.sleep(1.5)

img = ImageGrab.grab()
img.save(r'E:\Android exeperise\exeperise2\_shots\00_current.png')
print("saved", img.size)
