import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

T = 1.5

N = 200

up = 1
down = -1
field = [up, down]
colormap = colors.ListedColormap(["white","black"])

s = np.random.choice(field, N*N).reshape(N, N)

def update(data):
    global s, T
    newS = s.copy()

    for i in range (N):
        for j in range(N):
            sorroundSpin = (newS[i, (j-1)%N] + newS[i, (j+1)%N] + newS[(i-1)%N, j] + newS[(i+1)%N, j])
            E = -2*newS[i, j]*sorroundSpin

            if E>0:
                newS[i, j] *= -1
            else:
                r = np.random.rand()
                #print(r)
                if r < np.exp((2*E)/T):
                    newS[i, j] *= -1
    mat.set_data(newS)
    s = newS
    print("Simulating Generation ",data)
    return [mat]

fig, ax = plt.subplots()
mat = plt.imshow(s, cmap=colormap)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
#ani.save('randomLife.gif', writer='imagemagick', fps=60)
plt.show()

    
