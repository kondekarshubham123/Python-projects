import time
import pyautogui

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'Screenshot Data/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

screenshot()