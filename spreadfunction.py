import numpy as np
import math
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output

def viral_spread(population,time,initial):
  grid_space=int(math.sqrt(population))
  grid=np.zeros((grid_space,grid_space))
  for i in range(0,initial):
    x0=np.random.randint(0,grid_space-1) 
    y0=np.random.randint(0,grid_space-1)
    grid[x0,y0]=1

  plt.imshow(grid, interpolation='none', vmin=0, vmax=1, aspect='equal')

  ax = plt.gca();
  ax.set_xticks(np.arange(0, grid_space, 1));
  ax.set_yticks(np.arange(0, grid_space, 1));
  ax.set_xticklabels(np.arange(1, grid_space+1, 1));
  ax.set_yticklabels(np.arange(1, grid_space+1, 1));

  plot_list=[]
  infectioncount=[]
  for a in range(0,time): 
    for i in range(0,grid_space-1):
      for j in range(0,grid_space-1):
        if grid[i,j]==1:
          x_step=0
          y_step=0
          x_step=i+np.random.randint(-1,2)
          y_step=j+np.random.randint(-1,2)
          grid[x_step,y_step]=1

    infectioncount.append(np.count_nonzero(grid))
    plt.figure()
    plt.imshow(grid, interpolation='none', vmin=0, vmax=1, aspect='equal')
    plt.savefig('plot{}.png'.format(str(a)))
    plot_list.append('plot{}.png'.format(str(a)))
    plt.close()
  return [infectioncount[-1],plot_list]
