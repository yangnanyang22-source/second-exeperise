import ctypes
user32 = ctypes.windll.user32
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
titles = []
def cb(hwnd, lParam):
    length = user32.GetWindowTextLengthW(hwnd)
    if length > 0 and user32.IsWindowVisible(hwnd):
        buf = ctypes.create_unicode_buffer(length+1)
        user32.GetWindowTextW(hwnd, buf, length+1)
        titles.append((hwnd, buf.value))
    return True
user32.EnumWindows(EnumWindowsProc(cb), 0)
with open(r'E:\Android exeperise\exeperise2\_windows.txt', 'w', encoding='utf-8') as f:
    for hwnd, t in titles:
        f.write(f"{hwnd} | {t}\n")
print("done", len(titles))
