import random
import math

def conflicts(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def random_neighbor(state):
    n = len(state)
    col = random.randint(0, n - 1)
    row = random.randint(0, n - 1)
    while row == state[col]:
        row = random.randint(0, n - 1)
    new_state = state[:]
    new_state[col] = row
    return new_state

def simulated_annealing(n, max_steps=10000, initial_temp=1000, cooling_rate=0.995):
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_conf = conflicts(current)
    temp = initial_temp
    for step in range(max_steps):
        if current_conf == 0:
            return current
        neighbor = random_neighbor(current)
        neighbor_conf = conflicts(neighbor)
        delta = neighbor_conf - current_conf
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current = neighbor
            current_conf = neighbor_conf
        temp *= cooling_rate
    return None if current_conf > 0 else current

def solve_sa_with_restarts(n, max_restarts=100):
    random.seed()  # Optional: for reproducibility in testing
    for _ in range(max_restarts):
        solution = simulated_annealing(n)
        if solution:
            return solution
    return None

import matplotlib.pyplot as plt

def visualize_board(state):
    n = len(state)
    fig, ax = plt.subplots()
   
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, color="white"))
            else:
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, color="gray"))

    
    for col, row in enumerate(state):
        ax.text(col + 0.5, n - row - 0.5, "♛", ha="center", va="center", fontsize=24, color="red")

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()




# To solve:
n = 8
solution = solve_sa_with_restarts(n)
print(solution)

if solution:
    visualize_board(solution)



