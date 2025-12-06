import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#params
t_max, fps = 10, 30
# function to call from FuncAnimation
def animate(i):
    # plotting code!
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=int(t_max * fps), interval=1000 / fps)
# save mp4
ani.save('pendulum.mp4', writer='ffmpeg', fps=fps)
# save gif
ani.save('pendulum.gif', writer='imagemagick', fps=fps)
plt.show()
