import numpy as np
import matplotlib.pyplot as plt
# Used for numerical calculations and data visualization

Vac_rate=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
N=10000
beta=0.3
gamma=0.05
Infected=1
Susceptible=int((1-vac)*N-Infected) 
Recovered=0

for i in range(1,1001):
    infect_rate=Infected/N
   infected = susceptible * (1 - beta * infect_rate) + susceptible * beta * infect_rate
    susceptible -= infected
    recovered = infected * (1 - gamma) + recovered * gamma
    Infected += infected
    Recovered += recovered
# Generate a new number of infected individuals based on the current infection rate and number of infected individuals, and update the numbers of infected and uninfected individuals. Simultaneously perform similar processing on rehabilitation data
     
for index, value in enumerate(Vac_rate):
plt.plot(I, label=f"{value}%")
plt.xlabel("Time")
plt.ylabel("Number of Infected People")
plt.legend()
plt.title("SIR Model with Different Vaccination Rates")
plt.show()
