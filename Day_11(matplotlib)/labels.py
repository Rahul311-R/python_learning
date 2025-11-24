import matplotlib.pyplot as plt

x = [2,3,4,5,6,7]
y1= [3,4,4,5,3,2]
y2= [8,9,6,4,2,1]
y3= [3,6,8,5,1,5]

plt.title("Rahul Table",fontsize = 25,c = "purple",fontweight = "bold",family = "Times new roman")
plt.xlabel("kela",c = "red")
plt.ylabel("left la",c = "blue")

plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)

plt.show()