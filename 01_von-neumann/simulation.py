import random

# 1. Setup simulation parameters
p = 0.8
num_trials = 10000

# 2. Function to flip the biased coin
def flip_biased_coin():
    # random.random() returns a random float between 0.0 and 1.0
    if random.random() < p:
        return "H"  
    else:
        return "T"  

# 3. Function to implement Von Neumann's algorithm
def extract_fair_result():
    flips_count = 0
    while True:
        first_flip = flip_biased_coin()
        second_flip = flip_biased_coin()
        flips_count = flips_count + 2

        # If outcome is Heads-Tails -> declare Fair Heads
        if first_flip == "H" and second_flip == "T":
            return "Heads", flips_count
        
        # If outcome is Tails-Heads -> declare Fair Tails
        if first_flip == "T" and second_flip == "H":
            return "Tails", flips_count
        
        # If HH or TT occurs, the while loop automatically retries

# 4. Run the Monte Carlo simulation
heads_count = 0
tails_count = 0
total_flips = 0

print("Running simulation...")

for _ in range(num_trials):
    result, flips = extract_fair_result()
    total_flips = total_flips + flips
    
    if result == "Heads":
        heads_count = heads_count + 1
    else:
        tails_count = tails_count + 1

# 5. Print results 
print("--- SIMULATION RESULTS ---")
print("Original biased coin Heads probability:", p * 100, "%")
print("Total fair decisions generated:", num_trials)
print("Heads obtained:", heads_count, f"({heads_count / num_trials * 100:.2f}%)")
print("Tails obtained:", tails_count, f"({tails_count / num_trials * 100:.2f}%)")
print("Average flips used per fair decision:", total_flips / num_trials)
print("Theoretical expected flips (1 / (p * (1 - p))):", 1 / (p * (1 - p)))
