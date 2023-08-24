import matplotlib.pyplot as plt
import numpy as np
a = np.array([1,2,3,5])
gpa = [3.65,3.86,3.85,3.88,3.96]
namegpa = ["M.1 - 3 ","M.4 term 1","M.4 term 2","M.5 term 1","M.5 term 2"]


plt.title("Python create graf GPA 5 term",size=20)
plt.plot(namegpa,gpa,marker="s")
plt.legend(["GPA"])
plt.xlabel("Term",backgroundcolor="yellow")
plt.ylabel("grade/GPA",backgroundcolor="yellow")
plt.show()