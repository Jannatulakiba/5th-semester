import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ===============================
# Utility functions
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
    """Generate all neighbors by moving one queen to another row."""
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
# Stochastic Hill Climbing
# ===============================

def stochastic_hill_climb(n, max_steps=1000):
    """Randomly select better neighbors (stochastic hill climbing)."""
    current = random_board(n)
    path = [current]
    for _ in range(max_steps):
        current_h = heuristic(current)
        if current_h == 0:
            break
        neighbors = get_neighbors(current)
        better = [b for b in neighbors if heuristic(b) < current_h]
        if not better:
            break
        current = random.choice(better)
        path.append(current)
    return current, path

# ===============================
# Visualization
# ===============================

def animate_path(path, interval=600):
    """Animate N-Queens board evolution."""
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

N = 8  # You can change N (e.g. 4, 8, 10)
print(f"--- Stochastic Hill Climbing for N={N} ---")

solution, path = stochastic_hill_climb(N)
print("Final board:", solution)
print("Final heuristic:", heuristic(solution))
print(f"Steps: {len(path)}")

# Animate the solving process
animate_path(path)
