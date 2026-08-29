# 🟠 The Marble Swap / Color Matching Game

## 🎯 Problem Statement
You are given a line of **$N$ marbles**, where each marble is colored either **Red (R)** or **Blue (B)**. 

In one allowed move, you can pick any **two adjacent marbles** and swap their positions. 

### ❓ Question
What is the minimum number of adjacent swaps required to rearrange the marbles so that **all Red marbles are grouped together on the left**, and **all Blue marbles are grouped together on the right**?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Inversion Counting Proof</b></summary>

<br>

### 1. The Core Equivalence (Inversions)
Instead of thinking about moving Reds left and Blues right simultaneously, focus on a single color—say, **Red**. 

- Imagine our goal is to move all Red marbles to the leftmost available slots.
- Every time a Red marble has to "jump over" a Blue marble to move toward its target position on the left, it requires **exactly 1 adjacent swap**.
- Therefore, the minimum total number of adjacent swaps is precisely equal to the number of **inversions** between Red and Blue marbles: the total count of pairs $(i, j)$ such that a Blue marble appears at index $i$, a Red marble appears at index $j$, and $i < j$ (i.e., a Blue marble is currently sitting to the left of a Red marble that needs to pass it).

---

### 2. Algorithmic Calculation Method
To find the minimum swaps efficiently without simulating every single move:

1. **Scan the array from left to right** and keep a running count of how many Blue marbles you have encountered so far.
2. Whenever you encounter a **Red marble**, it must pass *all* the Blue marbles that currently sit to its left. 
3. Add the current count of passed Blue marbles to your total swap counter.
4. Sum these contributions across all Red marbles in the array.

---

### 3. Concrete Example
Consider the sequence: **`B, R, B, R, R`** (Total length $N = 5$, two Blues at indices 1 and 3, three Reds at indices 2, 4, 5).

- **1st Red** (at index 2): Has 1 Blue to its left (index 1). $\to \text{Swaps} = 1$
- **2nd Red** (at index 4): Has 2 Blues to its left (indices 1 and 3). $\to \text{Swaps} = 2$
- **3rd Red** (at index 5): Has 2 Blues to its left (indices 1 and 3). $\to \text{Swaps} = 2$

Total minimum adjacent swaps = $1 + 2 + 2 = \mathbf{5}$ swaps to achieve the sorted state **`R, R, R, B, B`**.

</details>
