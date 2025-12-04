import random

# --- GA Configuration ---
TARGET_PHRASE = "Human life is not easy life"
VALID_GENES = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!"#%&/()=?@${[]}'''
POPULATION_SIZE = 100
MUTATION_RATE = 0.01

# --- Helper Functions (Replaces class methods) ---

def create_individual():
    """Creates a new random individual (chromosome)."""
    return [random.choice(VALID_GENES) for _ in range(len(TARGET_PHRASE))]

def calculate_fitness(chromosome):
    """Calculates fitness score. Higher is better (more matches)."""
    score = 0
    for i in range(len(chromosome)):
        if chromosome[i] == TARGET_PHRASE[i]:
            score += 1
    return score

def crossover(parent1, parent2):
    """Creates a child by combining genes from two parents."""
    child_chromosome = []
    for i in range(len(TARGET_PHRASE)):
        # Randomly pick a gene from either parent1 or parent2
        if random.random() < 0.5:
            child_chromosome.append(parent1[i])
        else:
            child_chromosome.append(parent2[i])
    return child_chromosome

def mutate(chromosome):
    """Applies random mutations to a chromosome."""
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = random.choice(VALID_GENES)
    return chromosome

# --- Main Algorithm ---

def main():
    # 1. Initialization: Create the first random population
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    
    generation = 0
    max_fitness = len(TARGET_PHRASE)

    while True:
        generation += 1

        # 2. Evaluation: Calculate fitness for each individual and sort
        # We sort by fitness so the best individuals are at the front
        population.sort(key=lambda chrom: calculate_fitness(chrom), reverse=True)
        
        best_chromosome = population[0]
        best_fitness = calculate_fitness(best_chromosome)
        
        # Print the best result of the current generation
        best_string = "".join(best_chromosome)
        print(f"Gen {generation}: \"{best_string}\" | Fitness: {best_fitness}")

        # Check for solution
        if best_fitness == max_fitness:
            print(f"\nSolution found in generation {generation}!")
            break

        # 3. Selection & Reproduction: Create the next generation
        next_generation = []
        
        # Elitism: Keep the top 10% of the population
        elite_count = int(POPULATION_SIZE * 0.1)
        next_generation.extend(population[:elite_count])

        # Create the remaining 90% of the new population from the best parents
        offspring_count = POPULATION_SIZE - elite_count
        
        # Parents are selected from the top 50% of the current population
        parent_pool = population[:int(POPULATION_SIZE * 0.5)]

        for _ in range(offspring_count):
            parent1 = random.choice(parent_pool)
            parent2 = random.choice(parent_pool)
            
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        
        population = next_generation

if __name__ == '__main__':
    main()