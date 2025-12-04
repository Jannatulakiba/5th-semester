import random


def objective_function(x):
    return -(x ** 2) + 10 * x + 5


def create_individual():
    return random.uniform(-10, 10)


def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        return individual + random.uniform(-1, 1)
    return individual


def crossover(parent1, parent2):
    return (parent1 + parent2) / 2


def genetic_algorithm(pop_size=20, generations=50, mutation_rate=0.1):
    population = [create_individual() for _ in range(pop_size)]

    for gen in range(generations):

        fitness = [(objective_function(ind), ind) for ind in population]
        fitness.sort(reverse=True)

        new_population = [ind for (_, ind) in fitness[:pop_size // 2]]

        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(new_population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_ind = max(population, key=objective_function)
    return best_ind, objective_function(best_ind)


if __name__ == "__main__":
    best_x, best_value = genetic_algorithm()
    print(f"Best x: {best_x:.4f}, Value: {best_value:.4f}")
