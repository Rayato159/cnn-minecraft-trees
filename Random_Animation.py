from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import os

path = str(os.getcwd()) + "\\" + "Datasets"
Trees = np.load(os.path.join(path ,"Minecraft_Trees.npy"))

fig, ax = plt.subplots(1,2)

ax[0].set_title("Oak")
ax[0].imshow(Trees[0], cmap = "gray", interpolation = "nearest")
ax[1].set_title("Spruce")
ax[1].imshow(Trees[100], cmap = "gray", interpolation = "nearest")

def update(frame):
    ax[0].cla()
    ax[1].cla()

    ax[0].set_title("Oak")
    ax[0].imshow(Trees[frame], cmap = "gray", interpolation = "nearest")
    ax[1].set_title("Spruce")
    ax[1].imshow(Trees[frame+100], cmap = "gray", interpolation = "nearest")
    
    # plt.savefig("D:\Video\Graph\graph_"+str(section)+".png")

ani = FuncAnimation(fig, update, frames=range(1, 101, 1), interval=100, repeat=True)

plt.show()