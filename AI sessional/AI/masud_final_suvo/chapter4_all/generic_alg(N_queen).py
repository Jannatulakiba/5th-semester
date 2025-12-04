import random
import matplotlib.pyplot as plt

def random_perm(n):
    state = list(range(n))
    random.shuffle(state)
    return state

def conflicts(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks

def pmx_crossover(p1, p2):
    n = len(p1)
    c1, c2 = [-1] * n, [-1] * n
    start, end = sorted(random.sample(range(n), 2))
    c1[start:end] = p2[start:end]
    c2[start:end] = p1[start:end]
    mapping1 = {p2[i]: p1[i] for i in range(start, end)}
    mapping2 = {p1[i]: p2[i] for i in range(start, end)}
    for i in list(range(0, start)) + list(range(end, n)):
        val = p1[i]
        while val in c1[start:end]:
            val = mapping1.get(val, val)
        c1[i] = val
    for i in list(range(0, start)) + list(range(end, n)):
        val = p2[i]
        while val in c2[start:end]:
            val = mapping2.get(val, val)
        c2[i] = val
    return c1, c2

def mutate(state, prob=0.2):
    if random.random() < prob:
        i, j = random.sample(range(len(state)), 2)
        state[i], state[j] = state[j], state[i]
    return state

def genetic_algorithm(n, pop_size=100, generations=1000, mutation_prob=0.2, elitism=0.1):
    pop = [random_perm(n) for _ in range(pop_size)]
    for gen in range(generations):
        for ind in pop:
            if conflicts(ind) == 0:
                return ind
        pop.sort(key=conflicts)
        elite_count = int(elitism * pop_size)
        new_pop = pop[:elite_count]
        while len(new_pop) < pop_size:
            tourn_size = 5
            parent1 = min(random.sample(pop, tourn_size), key=conflicts)
            parent2 = min(random.sample(pop, tourn_size), key=conflicts)
            child1, child2 = pmx_crossover(parent1, parent2)
            mutate(child1, mutation_prob)
            mutate(child2, mutation_prob)
            new_pop.extend([child1, child2])
        pop = new_pop[:pop_size]
    best = min(pop, key=conflicts)
    return best if conflicts(best) == 0 else None

def solve_ga_with_restarts(n, max_restarts=10):
    random.seed()
    for _ in range(max_restarts):
        solution = genetic_algorithm(n)
        if solution:
            return solution
    return None

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

# To solve:
n = 8
solution = solve_ga_with_restarts(n)
print("Genetic Algorithm Solution:", solution, "Conflicts:", conflicts(solution) if solution else "N/A")

if solution:
    visualize_board(solution)
