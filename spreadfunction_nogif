import numpy as np
import math
import random
from IPython.display import clear_output

def viral_spread(population,hour,initial,movement):
  time =hour*4
  grid_space=int(math.sqrt(population))
  grid=np.zeros((grid_space,grid_space))
  for i in range(0,initial):
    x0=np.random.randint(0,grid_space-1) 
    y0=np.random.randint(0,grid_space-1)
    grid[x0,y0]=1

  spread_chance=[0]*94+[1]*6
  infectioncount=[]

  for a in range(0,time): 
    for i in range(0,grid_space-1):
      for j in range(0,grid_space-1):
        if grid[i,j]==1:
          for a in range(-1,2):
            for b in range (-1,2):
              grid[a,b] = random.choice(spread_chance)
          x_switch=0
          y_switch=0
          x_switch=i+np.random.randint(-movement,movement+1)
          y_switch=j+np.random.randint(-movement,movement+1)
          if x_switch < grid_space-1 & x_switch>0 & y_switch<grid_space-1 & y_switch> 0:
            grid[x_switch,y_switch]=1
            grid[i,j]=0

      infectioncount.append(np.count_nonzero(grid))
  return [infectioncount[-1]]
