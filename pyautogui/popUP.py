import pyautogui as at
#at.alert(text="Please enter",title="Please enter",button="NOT")
#at.confirm(title="Please enter",text="Please enter",buttons="A""b")
#title = at.prompt(title="Password",text="Password")
# title = at.password(title="Password",text="Input Password")
# print(title)
text = at.prompt(text='Do you like apples?', title='Question', default='YES')