import random
from copy import deepcopy
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# ----- Puzzle utilities -----
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)  # 0 = blank tile

def to_grid(state):
    return np.array(state).reshape((3,3))

def manhattan(state, goal=GOAL):
    # Sum of Manhattan distances for tiles 1..8
    s = 0
    for val in range(1,9):
        i = state.index(val)
        gi = goal.index(val)
        s += abs(i//3 - gi//3) + abs(i%3 - gi%3)
    return s

def neighbors(state):
    st = list(state)
    i = st.index(0)
    x, y = divmod(i, 3)
    moves = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            j = nx*3 + ny
            new = st.copy()
            new[i], new[j] = new[j], new[i]
            moves.append(tuple(new))
    return moves

def is_solvable(state):
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

# ----- Hill climbing algorithm -----
def hill_climb(start, max_iters=1000, sideways_limit=100, allow_sideways=True):
    current = start
    current_h = manhattan(list(current))
    path = [current]
    sideways = 0
    iters = 0

    while iters < max_iters and current_h != 0:
        iters += 1
        neighs = neighbors(current)
        scored = sorted([(manhattan(list(n)), n) for n in neighs], key=lambda x: x[0])
        best_h, best_n = scored[0]

        if best_h < current_h:
            current, current_h = best_n, best_h
            path.append(current)
            sideways = 0
        elif allow_sideways and best_h == current_h and sideways < sideways_limit:
            equal = [n for h, n in scored if h == current_h]
            chosen = random.choice(equal)
            current = chosen
            path.append(current)
            sideways += 1
        else:
            break

    return {"final": current, "h": current_h, "path": path, "iters": iters}

def random_restart_hill_climb(start, restarts=10, max_iters=1000):
    best_result = None
    for r in range(restarts):
        result = hill_climb(start, max_iters=max_iters)
        if best_result is None or result["h"] < best_result["h"]:
            best_result = result
            if best_result["h"] == 0:
                break
        # random restart with solvable shuffle
        s = list(start)
        while True:
            random.shuffle(s)
            if is_solvable(tuple(s)):
                start = tuple(s)
                break
    return best_result

# ----- Visualization -----
def show_path(path, interval=500, figsize=(4,4)):
    grids = [to_grid(list(state)) for state in path]
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_xticks([]); ax.set_yticks([])

    def update(i):
        ax.clear()
        ax.set_xticks([]); ax.set_yticks([])
        g = grids[i]
        tb = ax.table(cellText=g, loc='center', cellLoc='center')
        tb.scale(1, 2)
        ax.set_title(f"Step {i} / {len(grids)-1} | Manhattan = {manhattan(list(path[i]))}")
        return tb,

    ani = animation.FuncAnimation(fig, update, frames=len(grids), interval=interval, repeat=False)
    plt.show()
    return ani

# ----- Generate random solvable start -----
def shuffled_start(moves=30):
    state = list(GOAL)
    for _ in range(moves):
        state = list(random.choice(neighbors(tuple(state))))
    return tuple(state)

# ----- Example run -----
START = shuffled_start(40)
print("Start state:", START)
print("Solvable?", is_solvable(START))
print("Start heuristic (Manhattan):", manhattan(list(START)))

result = random_restart_hill_climb(START, restarts=15, max_iters=2000)
print("\nHill-climbing result:")
print("Final state:", result["final"])
print("Final heuristic:", result["h"])
print("Iterations:", result["iters"])
print("Path length:", len(result["path"]))

# Show animation
ani = show_path(result["path"], interval=600)
