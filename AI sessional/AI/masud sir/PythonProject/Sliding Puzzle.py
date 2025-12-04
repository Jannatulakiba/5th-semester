import copy

# Goal state
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Heuristic: number of misplaced tiles
def heuristic(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced


# Find position of blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate all possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors


# Hill Climbing algorithm
def hill_climbing(start_state):
    current = start_state
    steps = 0

    while True:
        print(f"\nStep {steps}, Heuristic: {heuristic(current)}")
        for row in current:
            print(row)
        print("-----")

        if heuristic(current) == 0:
            print("Goal reached!")
            return current

        neighbors = get_neighbors(current)
        neighbor = min(neighbors, key=heuristic)

        if heuristic(neighbor) >= heuristic(current):
            print("Reached local maximum. Cannot proceed further.")
            return current

        current = neighbor
        steps += 1


# Input initial state from user
print("Enter the initial 8-puzzle state row by row (use 0 for blank):")
start_state = []
for i in range(3):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    start_state.append(row)

# Run the algorithm
final_state = hill_climbing(start_state)
