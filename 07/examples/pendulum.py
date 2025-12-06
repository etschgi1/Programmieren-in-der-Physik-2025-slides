import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


length = 1.0  
theta0 = np.pi / 4  # initial angle 
omega0 = 0.0  # initial angular velocity 


t_max = 10  # maximum time (seconds)
fps = 30  # frames per second

def pendulum_position(t):
    theta = theta0 * np.cos(np.sqrt(9.8 / length) * t)  # simple HO
    return theta

def animate(i):
    ax.clear()
    t = i / fps
    theta = pendulum_position(t)
    x = length * np.sin(theta)
    y = -length * np.cos(theta)
    ax.plot([0, x], [0, y], lw=2, c='b')  # pendulum arm
    ax.plot(x, y, marker='o', markersize=10, c='r')  # pendulum bob
    ax.set_xlim(-1.5 * length, 1.5 * length)
    ax.set_ylim(-1.5 * length, 0.5 * length)
    ax.set_aspect('equal')
    ax.set_title('Pendulum Animation')


fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, animate, frames=int(t_max * fps), interval=1000 / fps)
# save mp4
# ani.save('pendulum.mp4', writer='ffmpeg', fps=fps)
# save gif
# ani.save('pendulum.gif', writer='imagemagick', fps=fps)
plt.show()
