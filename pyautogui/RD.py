import pyautogui as at,time
time.sleep(3)
for i in range(1,73):
        title = str(i)
        at.write(title)
        at.press('enter')