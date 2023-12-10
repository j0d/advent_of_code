import numpy as np
from scipy.optimize import minimize

# Constants and slopes
constants = np.array([21883, 19667, 14681, 16897, 13019, 11911])
slopes = np.array([16897, 11911, 14681, 13019, 21883, 19667])

# Objective function to minimize
# The function calculates the sum of squared differences between Y and each expression
def objective_function(Y):
    differences = Y - (constants + slopes * np.arange(1, len(constants) + 1))
    return np.sum(differences ** 2)

# Initial guess for Y
initial_guess = 0

# Perform the minimization
result = minimize(objective_function, initial_guess)

# Optimal value of Y
optimal_Y = result.x[0]
print("Optimal value of Y:", optimal_Y)
