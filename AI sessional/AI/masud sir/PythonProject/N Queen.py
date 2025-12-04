import heapq

N = 8


def conflicts(state):
    total = 0
    for r1 in range(len(state)):
        c1 = state[r1]
        if c1 == -1:
            continue
        for r2 in range(r1 + 1, len(state)):
            c2 = state[r2]
            if c2 == -1:
                continue
            if c1 == c2 or abs(c1 - c2) == abs(r1 - r2):
                total += 1
    return total


def a_star_eight_queen():
    start_state = [-1] * N
    pq = [(0, 0, start_state)]

    while pq:
        f, g, state = heapq.heappop(pq)
        if g == N and conflicts(state) == 0:
            return state

        row = g
        for col in range(N):
            new_state = state.copy()
            new_state[row] = col
            if conflicts(new_state) == 0:
                g_new = g + 1
                h_new = conflicts(new_state)
                f_new = g_new + h_new
                heapq.heappush(pq, (f_new, g_new, new_state))
    return None


solution = a_star_eight_queen()
if solution:
    print("One solution (row -> column):")
    for r, c in enumerate(solution):
        print(f"Row {r}: Col {c}")
else:
    print("No solution found.")