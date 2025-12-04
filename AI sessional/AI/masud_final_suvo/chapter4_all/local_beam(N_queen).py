import random

def conflicts(state):
    attacks = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def generate_random_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def get_neighbors(state):
    neighbors = []
    n = len(state)
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                new_state = state[:]
                new_state[col] = row
                neighbors.append(new_state)
    return neighbors

def local_beam_search(n, beam_width=4, max_steps=1000):
    beam = [generate_random_state(n) for _ in range(beam_width)]
    for step in range(max_steps):
        for state in beam:
            if conflicts(state) == 0:
                return state
        successors = []
        for state in beam:
            successors.extend(get_neighbors(state))
        successors.sort(key=conflicts)
        beam = successors[:beam_width]
    return None

def solve_lbs_with_restarts(n, max_restarts=100):
    random.seed()  # Optional: for reproducibility in testing
    for _ in range(max_restarts):
        solution = local_beam_search(n)
        if solution:
            return solution
    return None

import matplotlib.pyplot as plt

def visualize_board(state):
    n = len(state)
    fig, ax = plt.subplots()
    # 
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, color="white"))
            else:
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, color="gray"))

    # 
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
solution = solve_lbs_with_restarts(n)
print(solution)

if solution:
    visualize_board(solution)

