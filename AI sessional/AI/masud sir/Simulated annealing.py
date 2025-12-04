import math
import random

# 1. The function we want to find the minimum for.
# This is our "cost" or "objective" function.
def objective_function(x):
    """A simple function where the minimum is at x=0."""
    return x**2.0

# 2. The main Simulated Annealing algorithm
def simulated_annealing(bounds, iterations, step_size, initial_temp, cooling_rate):
    """
    Performs the simulated annealing optimization algorithm.
    """
    # Generate a random starting point within the given bounds
    current_solution = random.uniform(bounds[0], bounds[1])
    current_cost = objective_function(current_solution)

    # The best solution found so far is the starting point
    best_solution = current_solution
    best_cost = current_cost
    
    # Store history for plotting later (optional)
    history = []
    
    # Main loop of the algorithm
    temp = initial_temp
    for i in range(iterations):
        # Take a random step to find a "neighbor" solution
        candidate_solution = current_solution + random.uniform(-1, 1) * step_size
        
        # Ensure the candidate is within the problem bounds
        candidate_solution = max(min(candidate_solution, bounds[1]), bounds[0])

        # Calculate the cost of the new solution
        candidate_cost = objective_function(candidate_solution)

        # Check if this is the best solution we've seen so far
        if candidate_cost < best_cost:
            best_solution, best_cost = candidate_solution, candidate_cost
            print(f"> Iteration {i}, New Best: f({best_solution:.4f}) = {best_cost:.4f}")

        # Calculate the difference in cost between new and current solutions
        cost_difference = candidate_cost - current_cost

        # If the new solution is better, we always accept it.
        # If it's worse, we might still accept it based on a probability.
        # This probability is higher when the temperature is high.
        if cost_difference < 0:
             # Always accept a better solution
             current_solution, current_cost = candidate_solution, candidate_cost
        else:
            # Calculate acceptance probability for a worse solution
            acceptance_prob = math.exp(-cost_difference / temp)
            if random.random() < acceptance_prob:
                current_solution, current_cost = candidate_solution, candidate_cost

        # Cool down the temperature
        temp *= cooling_rate
        
        # Add the current best cost to our history
        history.append(best_cost)
        
    return best_solution, best_cost, history

# --- Main execution block ---
if __name__ == "__main__":
    # Define the problem bounds and algorithm parameters
    problem_bounds = [-5.0, 5.0]
    num_iterations = 1000
    movement_step_size = 0.1
    start_temp = 10.0
    alpha_cooling_rate = 0.99  # A value close to 1 is a "slow" cool down

    # Run the algorithm
    best_sol, best_val, cost_history = simulated_annealing(
        problem_bounds, num_iterations, movement_step_size, start_temp, alpha_cooling_rate
    )
    
    print("\nDone!")
    print(f"Best Solution Found: x = {best_sol:.5f}")
    print(f"Minimum Value Found: f(x) = {best_val:.5f}")