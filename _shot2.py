import ctypes, time
from PIL import ImageGrab

user32 = ctypes.windll.user32
hwnd = 132646

def activate():
    user32.SetForegroundWindow(hwnd)
    time.sleep(0.5)

def shot(name):
    img = ImageGrab.grab()
    p = rf'E:\Android exeperise\exeperise2\_shots\{name}.png'
    img.save(p)
    print("saved", p)

# 1. 先截当前 activity_main.xml + 模拟器运行效果
activate()
time.sleep(0.5)
shot("01_activity_main_xml_and_running")

# 2. 用 Ctrl+Shift+N 打开 strings.xml
import subprocess
activate()
# Ctrl+Shift+N
ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)  # ctrl
ctypes.windll.user32.keybd_event(0x10, 0, 0, 0)  # shift
ctypes.windll.user32.keybd_event(0x4E, 0, 0, 0)  # N
time.sleep(0.1)
ctypes.windll.user32.keybd_event(0x4E, 0, 2, 0)
ctypes.windll.user32.keybd_event(0x10, 0, 2, 0)
ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)
time.sleep(1.0)
# 输入 strings.xml
ctypes.windll.user32.keybd_event(0x53, 0, 0, 0)  # S
time.sleep(0.05)
# 用剪贴板输入中文更靠谱
user32 = ctypes.windll.user32
import subprocess as sp
# 直接用 keybd_event 输入太慢，用 SetClipboardData
# 简单点：用 type 方式不可靠，改用剪贴板
sp.run(['clip'], input='strings.xml', text=True)
time.sleep(0.2)
# Ctrl+V
ctypes.windll.user32.keybd_event(0x11, 0, 0, 0)
ctypes.windll.user32.keybd_event(0x56, 0, 0, 0)
time.sleep(0.1)
ctypes.windll.user32.keybd_event(0x56, 0, 2, 0)
ctypes.windll.user32.keybd_event(0x11, 0, 2, 0)
time.sleep(0.8)
# Enter
ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)
time.sleep(0.1)
ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
time.sleep(1.5)
shot("02_strings_xml")
