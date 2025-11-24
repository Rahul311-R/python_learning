import matplotlib.pyplot as plt

event = ["sport","dance","singing","drawing","writing"]
part = [234,245,176,326,297]
color = ["purple","yellow","orange","blue","pink"]

plt.pie(part,labels=event,autopct="%1.1f%%",colors=color,
explode = [0, 0, 0, 0.1,0],
shadow = True,
startangle = 90)

plt.show()