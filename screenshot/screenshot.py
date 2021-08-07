import time
import pyautogui

def screenshot():
    file_name = int(round(time.time()*200))
    file_name = f'{file_name}.png'
    time.sleep(5)
    screenshot_img = pyautogui.screenshot(file_name)
    screenshot_img.show()

screenshot()
