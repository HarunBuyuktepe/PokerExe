from random import randrange
import win32api, win32con
import time
import sys; print(sys.executable)
def poker():
    pos = win32api.GetCursorPos()
    print(pos)
    print('Width:', win32api.GetSystemMetrics(0))
    maxwidth = win32api.GetSystemMetrics(0)
    print('Height:', win32api.GetSystemMetrics(1))
    maxheight = win32api.GetSystemMetrics(1)
    x = pos[0]
    y = pos[1]
    print('x = ',x , ' y = ',y)
    while True:

        x = randrange(maxwidth)
        y = randrange(maxheight)
        
        while x >= maxwidth:
            x = 0
        while y >= maxheight:
            y = 0
            
        print('x = ',x , ' y = ',y)
        time.sleep(3)
        win32api.SetCursorPos((x, y))



poker()
