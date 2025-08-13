import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def kink(x, t, v=0.5, x0=0.0):
    gamma = 1.0 / np.sqrt(1.0 - v**2)
    arg = gamma * (x - v*t - x0)
    return 4.0 * np.arctan(np.exp(arg))

v = 0.5           
x0 = -15.0       
x = np.linspace(-80, 80, 1500)

fig, ax = plt.subplots(figsize=(8,4))
y0 = kink(x, 0.0, v=v, x0=x0)
line, = ax.plot(x, y0, lw=2)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-0.5, 2*np.pi + 0.5)     
ax.set_yticks([0, np.pi, 2*np.pi])
ax.set_yticklabels(['0', 'π', '2π'])
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")

tmax = 40.0
nframes = 400
times = np.linspace(0.0, tmax, nframes)

def update(t):
    y = kink(x, t, v=v, x0=x0)
    line.set_ydata(y)
    return (line,)

ani = animation.FuncAnimation(fig, update, frames=times, interval=30, blit=True)
plt.show()
