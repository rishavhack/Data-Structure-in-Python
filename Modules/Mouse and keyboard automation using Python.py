import pyautogui
print pyautogui.size()
pyautogui.moveTo(100,100,duration=1)
pyautogui.moveRel(0,50,duration=1)
print pyautogui.position()
pyautogui.click(100,100)

import time
time.sleep(10)
pyautogui.moveTo(100,0,duration=1)
pyautogui.dragRel(100,0,duration=1)
pyautogui.dragRel(0, 100, duration=1)
pyautogui.dragRel(-100, 0, duration=1)
pyautogui.dragRel(0, -100, duration=1)

pyautogui.scroll(200)

pyautogui.click(100, 100)
