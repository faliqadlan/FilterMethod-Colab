# Import the required library
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the harmonic potential
xmin = -10 # Lower bound of the x domain
xmax = 10 # Upper bound of the x domain
dx = 0.001 # Distance between x grids
k = 1 # Spring constant or Omega
v0 = 0 # Potential value at zero point
leb = xmax-xmin # Length of the x domain
ngrid = int(leb/dx) # Number of x grids

# Create arrays for x coordinates and v potential
x = np.zeros(ngrid)
v = np.zeros(ngrid)

# Define a function to calculate the harmonic potential
def potensial_harmonik(x, k, v0):
  # x is an array of x coordinates
  # k is the spring constant
  # v0 is the potential value at zero point
  # This function returns an array of v potential that corresponds to x, k, and v0
  v = 0.5 * k * x ** 2 + v0 # Formula for harmonic potential
  return v

# Calculate the harmonic potential for each x value
for i in range(0,ngrid):
  x[i] = xmin + (i * dx) # The i-th x coordinate
  v[i] = potensial_harmonik(x[i], k, v0) # The i-th v potential

# Plot the harmonic potential versus x
plt.figure(figsize=(10,6)) # Create a figure with size 10x6 inches
plt.plot(x,v, label='Harmonic Potential') # Plot a line with label Harmonic Potential
plt.xlabel('x') # Label the x axis
plt.ylabel('v') # Label the y axis
plt.title('Harmonic Potential versus x') # Give a title to the plot
plt.legend() # Show the plot legend
plt.show() # Show the plot
