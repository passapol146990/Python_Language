input_score = int(input("Input Grade : "))
def grad_calculate(input_score):#พัสพล py
    gradLaber = "FFFFFDCBAAAAA"
    print((input_score < 0 or input_score > 100) and "erre" or gradLaber[input_score//10])

grad_calculate(input_score)