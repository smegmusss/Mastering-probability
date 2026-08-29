# 🟠 25 Horses and 5 Lanes Puzzle

## 🎯 Problem Statement
You have **25 horses** of different, constant speeds, and a race track with **5 lanes**.
- This means at most **5 horses** can race against each other at the same time.
- You **do not have a stopwatch** or any timing device; you can only observe the relative finishing order (1st, 2nd, 3rd, 4th, 5th) of horses in any given race.

### ❓ Question
What is the **minimum number of races** required to determine with 100% certainty the **fastest 3 horses** among the entire group of 25, and what is the optimal strategy?

---

<details>
<summary><b>💡 Click to Reveal the Optimal 7-Race Solution & Proof</b></summary>

<br>

### 1. Phase 1: Group Stage (5 Races)
Divide the 25 horses into 5 arbitrary groups of 5 horses each ($A, B, C, D, E$).
* Run a race for each group. This consumes **5 races**.
* After these races, we know the internal ranking of each group. Let's denote the horses in Group A as $A_1, A_2, A_3, A_4, A_5$ (where $A_1$ is the fastest in group A, $A_2$ is second, etc.).

---

### 2. Phase 2: The Winners' Race (Race 6)
* Take the winner from each group: $A_1, B_1, C_1, D_1, E_1$.
* Run a 6th race with these 5 horses. This consumes **1 race** (Total = 6 races).

Without loss of generality, suppose the finishing order of this winners' race is:
$$A_1 > B_1 > C_1 > D_1 > E_1$$

#### What can we immediately eliminate?
1. **$D_1, E_1$ and all their subordinates** cannot be in the top 3 overall. 
   - Since $D_1$ came behind $A_1$ and $B_1$, and there are at least two horses faster than $D_1$ ($A_1, B_1$), $D_1$ and $E_1$ are out. We discard $D_2, D_3, D_4, D_5, E_1, E_2, E_3, E_4, E_5$.
2. **$C_1$ and its subordinates ($C_2, C_3$)** cannot be in the top 3 because $A_1$ and $B_1$ are already faster than $C_1$.
3. **$B_2, B_3$**: Can they be in the top 3? Yes, potentially 3rd overall.
4. **$A_2, A_3$**: Can they be in the top 3? Yes, potentially 2nd or 3rd overall.

---

### 3. Phase 3: The Final Contender Race (Race 7)
We are left with exactly **5 candidate horses** that could possibly occupy 2nd and 3rd place overall:
- $A_2, A_3$ (from Group A)
- $B_1, B_2$ (from Group B)
- $C_1$ (from Group C)

*Note: $A_1$ is already guaranteed 1st overall, so we don't need to race him again.*

* Run a 7th race with these 5 candidates: **$(A_2, A_3, B_1, B_2, C_1)$**. This consumes the **7th and final race**.
* The top 2 finishers of this 7th race (along with $A_1$) form the definitive **top 3 fastest horses** out of all 25.

</details>
