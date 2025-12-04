import random

def f(x):
    return -(x-3)**2 + 9   # peak at x=3

def hill_climb():
    x = random.uniform(-10, 10)   # random start
    step = 0.1
    for _ in range(1000):
        new_x = x + random.choice([-step, step])
        if f(new_x) > f(x):   # move if better
            x = new_x
    return x, f(x)

best_x, best_val = hill_climb()
print("Best x:", round(best_x, 2), "f(x):", round(best_val, 2))
