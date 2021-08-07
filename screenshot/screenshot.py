import time
import pyautogui
import tkinter as tk

def screenshot():
    file_name = int(round(time.time()*200))
    file_name = f'{file_name}.png'
    time.sleep(5)
    screenshot_img = pyautogui.screenshot(file_name)
    screenshot_img.show()


def screenshot2():
    file_name = int(round(time.time()*200))
    file_name = f'{file_name}.png'
    time.sleep(5)
    screenshot_img = pyautogui.screenshot(file_name)
    screenshot_img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = 'Take a screenshot',
    command=screenshot2
)

button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="QUIT",
    command=quit
)

close.pack(side=tk.LEFT)

root.mainloop()