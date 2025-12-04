import random
def objective_function(x):
    return -(x**2) + 10*x + 5 # -x² + 10x + 5

def hill_climbing(max_iterations=100, step_size=0.1):
    current_x = random.uniform(-10, 10)
    current_value = objective_function(current_x)

    for i in range(max_iterations):
        neighbor_x = current_x + random.uniform(-step_size, step_size)
        neighbor_value = objective_function(neighbor_x)

        if neighbor_value > current_value:
            current_x, current_value = neighbor_x, neighbor_value
    return current_x, current_value

if __name__ == "__main__":
    best_x, best_value = hill_climbing()
    print(f"max x: {best_x:.4f}, function : {best_value:.4f}")