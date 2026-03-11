import random

# -----------------------------
# Problem Data
# -----------------------------
weights = [10, 20, 30, 15, 25]
values = [60, 100, 120, 70, 90]
capacity = 50

num_items = len(weights)

POP_SIZE = 10
GENERATIONS = 50
MUTATION_RATE = 0.1

# -----------------------------
# Create Random Chromosome
# -----------------------------
def create_chromosome():
    return [random.randint(0,1) for _ in range(num_items)]

# -----------------------------
# Initial Population
# -----------------------------
def create_population():
    return [create_chromosome() for _ in range(POP_SIZE)]

# -----------------------------
# Fitness Function
# -----------------------------
def fitness(chromosome):
    total_weight = 0
    total_value = 0

    for i in range(num_items):
        if chromosome[i] == 1:
            total_weight += weights[i]
            total_value += values[i]

    if total_weight > capacity:
        return 0
    return total_value

# -----------------------------
# Tournament Selection
# -----------------------------
def selection(population):
    a = random.choice(population)
    b = random.choice(population)

    if fitness(a) > fitness(b):
        return a
    return b

# -----------------------------
# Single Point Crossover
# -----------------------------
def crossover(parent1, parent2):
    point = num_items // 2

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2

# -----------------------------
# Mutation (bit flip)
# -----------------------------
def mutation(chromosome):
    for i in range(num_items):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# -----------------------------
# Genetic Algorithm
# -----------------------------
population = create_population()

best_solution = None
best_fitness = 0

for generation in range(GENERATIONS):

    new_population = []

    while len(new_population) < POP_SIZE:

        parent1 = selection(population)
        parent2 = selection(population)

        child1, child2 = crossover(parent1, parent2)

        child1 = mutation(child1)
        child2 = mutation(child2)

        new_population.append(child1)
        new_population.append(child2)

    population = new_population[:POP_SIZE]

    for chrom in population:
        f = fitness(chrom)
        if f > best_fitness:
            best_fitness = f
            best_solution = chrom

# -----------------------------
# Result
# -----------------------------
print("Best Solution:", best_solution)
print("Maximum Value:", best_fitness)

total_weight = sum(weights[i] for i in range(num_items) if best_solution[i]==1)
print("Total Weight:", total_weight)