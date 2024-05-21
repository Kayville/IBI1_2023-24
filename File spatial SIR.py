import numpy as np
import matplotlib.pyplot as plt
#Used for numerical calculations and data visualization

beta=0.3 
gamma=0.05
population = np.zeros((100, 100), dtype=np.bool)
infected = np.random.choice([False]*100, 2, replace=False) 
infected[0] = True  
fig = plt.figure(figsize=(width, height), dpi=dpi)
im = plt.imshow(population, cmap, interpolation)  
plt.title("Select One to be Infected Randomly.") 
plt.show()
plt.clf() 
# Boolean, binary array that intuitively represents the population infection situation and the number of infected individuals

time_range = range(1, 101)
infected_indices = np.where(population == 1)
for infected_index in infected_indices[0]:
    x = infected_index
    y = infected_indices[1][infected_index]
    for x_neighbour in range(x - 1, x + 2):
        for y_neighbour in range(y - 1, y + 2):
            if (x_neighbour, y_neighbour) != (x, y):
                if population[x_neighbour, y_neighbour] == 0:
                    population[x_neighbour, y_neighbour] = np.random.choice(range(2), 1, p=[1 - beta, beta])[0]
 recover_indices = np.random.choice([0, 1], len(infected_indices[0]), p=[1 - gamma, gamma])
recover_indices = infected_indices[recover_indices == 1]
population[recover_indices[0], recover_indices[1]] = 2
# First, identify the current infected location, and then randomly select some people from the neighbors of these locations to be infected and some people to recover based on probability. Mark the recovered locations as 2, indicating that the people in these locations have recovered.

if time in [10, 50, 100]:
    plt.imshow(population, cmap="viridis", interpolation="nearest")
    plt.title(f"Spatial SIR Model Results for {time} repeats.")
    plt.show()                   
 
   
