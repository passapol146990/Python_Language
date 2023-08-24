import matplotlib.pyplot as plt
name = ["python","vaja","html","c#","drat"]
score1 = [5,2,5,3,1]
score2 = [1,2,3,4,5]

plt.title("Passapol!")
plt.bar(name,score1,width=0.5,color='b',edgecolor='black')
plt.xlabel("Language")
plt.ylabel("Leval")
plt.figure()
plt.title("Passapol!")
plt.pie(score1,labels=name,autopct="%.2f%%")

plt.show()