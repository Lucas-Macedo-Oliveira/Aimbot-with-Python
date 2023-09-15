import pyautogui
import keyboard
import win32api, win32con
import time


def click(x,y):
    #usando api do windows pq é mais rapido, click do pyautogui é mt lento
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('c')== False:
    print('começou a percorrer o SC')
    sc = pyautogui.screenshot(region=(180,280,635,500))
    sc.save('example.jpg')
    widht,height = sc.size

    for x in range(0,widht,10):
        achou = 0
        for y in range(0,height,10):
            r,g,b = sc.getpixel((x,y))
            print(sc.getpixel((x,y)))

            if r == 255 and g == 219 and b == 195:
                achou = 1
                #pyautogui.click(98+x,365+y)
                click(180+x,280+y)
                time.sleep(0.01)
                break
        if achou ==1:
            break

#255,219,195