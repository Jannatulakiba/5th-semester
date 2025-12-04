import math
import random


def objective_function(x):
    return x ** 2 + 10 * math.sin(x)  # (example: f(x) = x^2 + 10*sin(x))


def simulated_annealing(objective, bounds, max_iter, initial_temp, cooling_rate):
    current_x = random.uniform(bounds[0], bounds[1])
    current_energy = objective(current_x)

    best_x = current_x
    best_energy = current_energy

    temp = initial_temp

    for i in range(max_iter):

        new_x = current_x + random.uniform(-1, 1)
        new_x = max(bounds[0], min(bounds[1], new_x))

        new_energy = objective(new_x)

        delta_e = new_energy - current_energy

        if delta_e < 0 or random.random() < math.exp(-delta_e / temp):
            current_x = new_x
            current_energy = new_energy

            if new_energy < best_energy:
                best_x = new_x
                best_energy = new_energy

        temp = temp * cooling_rate

    return best_x, best_energy


best_solution, best_value = simulated_annealing(
    objective_function,
    bounds=[-10, 10],
    max_iter=1000,
    initial_temp=100,
    cooling_rate=0.99
)
print("Best Solution:", best_solution)
print("Best Value:", best_value)