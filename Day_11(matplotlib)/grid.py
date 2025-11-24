import matplotlib.pyplot as plt


x = [2,3,4,5,6,7]
y1= [3,4,4,5,3,2]
y2= [8,9,6,4,2,1]
y3= [3,6,8,5,1,5]

plt.grid(axis="y",linewidth = 3,c = "orange",linestyle = "dotted")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()