from tkinter import*
import random
def rule (p1_shape, p2_shape):
    if p1_shape == p2_shape:
        return "tied"
    elif (p1_shape == "rock" and p2_shape == "scissors")or(p1_shape=='paper' and p2_shape=='rock')or(p1_shape=='scissors' and p2_shape=='paper'):
        return "you win"
    else:
        return "you lost"

def game():
    def y1():
        a1 = "rock"
        x(a1)

    def y2():
        a1 = "paper"
        x(a1)

    def y3():
        a1 = "scissors"
        x(a1)

    def x(cha):

        bb = ['rock', 'paper', 'scissors']
        va = random.choice(bb)
        on = rule(cha,va)
        def hol(f):
            lable = Label(text=f,font=20)
            lable.grid(column=2, row=2)
        hol("\t")
        hol(on)
        return on

    def pol():
        root = Tk()
        t1 = Button(master=root, text="Rock", font=20, command=y1)
        t2 = Button(master=root, text="paper", font=20, command=y2)
        t3 = Button(master=root, text="scissors", font=20, command=y3)
        t1.grid(column=1, row=1)
        t2.grid(column=2, row=1)
        t3.grid(column=3, row=1)
        lable = Label(master=root,text="\t\t ")
        lable.grid(column=2, row=2)
        root.mainloop()


    pol()


game()
#if __name__ == '__main__':
#    print()
#    print()
#    print()