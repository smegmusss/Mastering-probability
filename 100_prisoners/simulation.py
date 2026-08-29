import random

def run_single_simulation(num_prisoners=100, max_tries=50):
#generating a random permutation from 1 to 99
    boxes = list(range(num_prisoners))
    random.shuffle(boxes)
    
    
    for prisoner in range(num_prisoners):
        current_box = prisoner
        found = False
        
        for _ in range(max_tries):
            card = boxes[current_box]
            if card == prisoner:
                found = True
                break
            current_box = card  # go to the corrispondent box
            
        if not found:
            return False  
            
    return True  

# Monte-Carlo simulation
num_simulations = 10000
success_count = 0

print("Running 100 Prisoners simulation...")
for _ in range(num_simulations):
    if run_single_simulation():
        success_count += 1

empirical_p = success_count / num_simulations
print("--- RESULTS ---")
print(f"Total trials: {num_simulations}")
print(f"Successful escapes: {success_count}")
print(f"Empirical Survival Probability: {empirical_p * 100:.2f}%")
print("Theoretical Survival Probability: ~31.18%")
