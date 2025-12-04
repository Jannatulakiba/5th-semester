import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ===============================
# Utility Functions
# ===============================

def random_board(n):
    """Generate a random board configuration."""
    return [random.randint(0, n - 1) for _ in range(n)]

def heuristic(board):
    """Count number of attacking queen pairs."""
    h = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h

def get_neighbors(board):
    """Generate all neighbors by moving one queen in its column."""
    n = len(board)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if row != board[col]:
                new_board = board.copy()
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

# ===============================
# Hill Climbing (single run)
# ===============================

def hill_climb_once(n, max_steps=1000):
    """Standard hill climbing: picks the best neighbor at each step."""
    current = random_board(n)
    path = [current]

    for _ in range(max_steps):
        current_h = heuristic(current)
        if current_h == 0:
            break

        neighbors = get_neighbors(current)
        best = min(neighbors, key=lambda x: heuristic(x))
        best_h = heuristic(best)

        if best_h < current_h:
            current = best
            path.append(current)
        else:
            break  # no improvement possible

    return current, path

# ===============================
# Random Restart Hill Climbing
# ===============================

def random_restart_hill_climb(n, restarts=10, max_steps=1000):
    """Repeats hill climbing from random initial states until solved."""
    best = None
    best_h = float('inf')
    best_path = []

    for r in range(restarts):
        current, path = hill_climb_once(n, max_steps)
        current_h = heuristic(current)

        print(f"Restart {r+1}: heuristic = {current_h}")

        if current_h < best_h:
            best = current
            best_h = current_h
            best_path = path

        if best_h == 0:  # solution found
            break

    return best, best_path

# ===============================
# Visualization
# ===============================

def animate_path(path, interval=600):
    """Animate the board evolution."""
    n = len(path[0])
    fig, ax = plt.subplots()
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(-0.5, n - 0.5)

    queens = [plt.Circle((0, 0), 0.3, color='black') for _ in range(n)]
    for q in queens:
        ax.add_patch(q)

    def update(i):
        board = path[i]
        for col, row in enumerate(board):
            queens[col].center = (col, n - 1 - row)
        ax.set_title(f"Step {i} | h={heuristic(board)}")
        return queens

    ani = animation.FuncAnimation(fig, update, frames=len(path),
                                  interval=interval, blit=True, repeat=False)
    plt.show()
    return ani

# ===============================
# Run Example
# ===============================

N = 8  # You can change N (e.g., 4, 8, 10)
print(f"--- Random-Restart Hill Climbing for N={N} ---")

solution, path = random_restart_hill_climb(N, restarts=15, max_steps=2000)
print("\nFinal board:", solution)
print("Final heuristic:", heuristic(solution))
print(f"Total steps (best run): {len(path)}")

# Visualize best run
animate_path(path)
