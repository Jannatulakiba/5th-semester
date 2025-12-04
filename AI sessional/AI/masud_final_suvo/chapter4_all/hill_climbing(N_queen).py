import random
import matplotlib.pyplot as plt

def conflicts(state):
    n = len(state)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                cnt += 1
    return cnt

def neighbors(state):
    n = len(state)
    result = []
    for col in range(n):
        for row in range(n):
            if row != state[col]:
                s = state.copy()
                s[col] = row
                result.append(s)
    return result

def hill_climbing(n=8, max_restarts=200, max_iters=500):
    for restart in range(max_restarts):
        state = [random.randrange(n) for _ in range(n)]
        for it in range(max_iters):
            if conflicts(state) == 0:
                return state
            nbrs = neighbors(state)
            best = min(nbrs, key=conflicts)
            if conflicts(best) >= conflicts(state):
                break  # stuck
            state = best
    return state  # best found

# 🔵 Visualization Function
def visualize_board(state):
    n = len(state)
    fig, ax = plt.subplots()
   
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, color=color))
    
    for col, row in enumerate(state):
        ax.text(col + 0.5, n - row - 0.5, "♛", ha="center", va="center", fontsize=24, color="red")

    ax.set_xlim(0, n)
    ax.set_ylim(0, n)
    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().set_aspect("equal", adjustable="box")
    plt.show()

# Example run
solution = hill_climbing()
print("Hill Climbing Solution:", solution, "Conflicts:", conflicts(solution))

if solution:
    visualize_board(solution)
