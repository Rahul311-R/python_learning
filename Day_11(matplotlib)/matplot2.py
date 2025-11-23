import matplotlib.pyplot as plt

x = [20,21,22,23,24,25]
y1 = [3,5,1,9,6,7]
y2 = [4,6,4,3,3,3]

style1 = dict(marker = ".",
         ms = 20,mfc = "black",
         mec = "red",ls = "dashdot",
         lw = 3,c = "cyan")
style2 = dict(marker = ">",mfc = "blue"
              ,mec = "green",c = "red",
              ls = "dotted",ms = 10,lw =2)
plt.plot(x,y1,**style1)
plt.plot(x,y2,**style2)
plt.show()