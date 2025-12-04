import heapq

def evaluate_state(state):
    return eval(state)
def beam_search(start, beam_width=2, max_depth=5):
    states = [(evaluate_state(start), start)]
    for depth in range(max_depth):
        new_states = []
        for value, state in states:
            for move in ["+1", "+2", "-1"]:
                new_state = state + move
                new_value = evaluate_state(new_state)
                new_states.append((new_value, new_state))
        states = heapq.nlargest(beam_width, new_states, key=lambda x: x[0])
    return states[0]
if __name__ == "__main__":
    best_value, best_state = beam_search("0", beam_width=3, max_depth=4)
    print(f"Best state: {best_state}, Value: {best_value}")
