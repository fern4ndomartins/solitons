import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def soliton(x, t, c=1.0, x0=0.0):
    arg = np.sqrt(c)/2 * (x - c*t - x0)
    return (c/2) * (1/np.cosh(arg))**2

c = 5
x0 = -10.0
x = np.linspace(-60, 60, 1000)

fig, ax = plt.subplots(figsize=(8,4))
y0 = soliton(x, 0.0, c=c, x0=x0)
line, = ax.plot(x, y0, lw=2)
ax.set_xlim(x.min(), x.max())
ax.set_ylim(0, 1.2*(c/2))  
ax.grid(True)
ax.set_xlabel("x")
ax.set_ylabel("u(x,t)")

tmax = 40.0
nframes = 400
times = np.linspace(0.0, tmax, nframes)

def update(t):
    y = soliton(x, t, c=c, x0=x0)
    line.set_ydata(y)
    return (line,)

ani = animation.FuncAnimation(fig, update, frames=times, interval=30, blit=True)

ani.save('soliton.mp4', writer='ffmpeg', fps=30, dpi=150)
plt.show()
