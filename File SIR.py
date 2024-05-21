import numpy as np
import matplotlib.pyplot as plt
# Used for numerical calculations and plotting
N = 10000 
beta = 0.3 
gamma = 0.05
Infected = 1
Susceptible = 9999 
Recovered = 0

for i in range(1, 101):
    infect_rate = Infected / N
    Infected  = int(np.random.choice(range(2), Susceptible, p=[1 - beta * infect_rate, beta * infect_rate]))  
    Infected += Infected 
    Susceptible -= Infected 
    Recovered = int(np.random.choice(range(2), Infected, p=(1 - gamma, gamma))) 
    Recovered += Recovered
# Firstly, calculate the current infection rate, and then use a function to generate a randomly selected sequence to determine the new number of infections. Then obtain the total number of infected individuals and susceptible individuals. Simultaneously use a similar method to calculate the new number of rehabilitation patients and obtain the total number of rehabilitation patients.

plt.plot( label="Recovered,Susceptible,Infected")
plt.xlabel("Time") 
plt.title("SIR Model") 
plt.ylabel("Number of people") 
plt.legend()  
plt.show() 
