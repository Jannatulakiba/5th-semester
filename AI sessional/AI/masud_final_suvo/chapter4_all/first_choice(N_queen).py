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

# ===============================
# First-Choice Hill Climbing
# ===============================

def first_choice_hill_climb(n, max_steps=1000):
    """
    First-Choice Hill Climbing:
    Randomly samples neighbors until a better one is found.
    """
    current = random_board(n)
    path = [current]

    for step in range(max_steps):
        current_h = heuristic(current)
        if current_h == 0:
            break

        improved = False
        for _ in range(n * n):  # randomly sample possible moves
            neighbor = current.copy()
            col = random.randint(0, n - 1)
            row = random.randint(0, n - 1)
            neighbor[col] = row
            if heuristic(neighbor) < current_h:
                current = neighbor
                improved = True
                break

        path.append(current)
        if not improved:
            break  # stuck in local minimum

    return current, path

# ===============================
# Visualization
# ===============================

def animate_path(path, interval=600):
    """Animate the path of the queens' movements."""
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
print(f"--- First-Choice Hill Climbing for N={N} ---")

solution, path = first_choice_hill_climb(N)
print("Final board:", solution)
print("Final heuristic:", heuristic(solution))
print(f"Steps taken: {len(path)}")

# Show animation
animate_path(path)
