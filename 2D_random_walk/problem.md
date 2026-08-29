# 🟠 2D Random Walk Paths with Non-Negative Constraints (Dyck Paths / Ballot Problem Variant)

## 🎯 Problem Statement
A frog starts at the origin $(0,0)$ on a two-dimensional grid and makes a sequence of **$10$ steps**. 
- In each step, the frog can move either **Right (+1, 0)**, **Left (-1, 0)**, **Up (0, +1)**, or **Down (0, -1)** with equal probability (or generally, we consider the combinatorics of all paths).
- **The Constraint:** The frog is **strictly forbidden** from entering negative coordinates on either axis ($x \ge 0$ and $y \ge 0$ at all times).
- **The Goal:** We want to count the number of distinct paths of length $10$ that start at $(0,0)$, stay entirely within the non-negative quadrant ($x, y \ge 0$), and **return to the origin $(0,0)$** at the end of the 10 steps.

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Reflection Principle</b></summary>

<br>

### 1. Decoupling the 2D Grid into Independent 1D Paths
A key property of a grid random walk with orthogonal steps is that movement along the $X$-axis and movement along the $Y$-axis are **completely independent**. 

To return to $(0,0)$ after $10$ total steps while staying in the non-negative quadrant ($x \ge 0$ and $y \ge 0$):
1. The frog must make a certain number of horizontal steps ($2k$ steps total: $k$ steps Right and $k$ steps Left) and vertical steps ($2(5-k)$ steps total: $(5-k)$ steps Up and $(5-k)$ steps Down).
2. **Crucial Constraint:** *Both* the $X$-coordinate path and the $Y$-coordinate path must independently remain non-negative ($x_t \ge 0$ for all $t$ and $y_t \ge 0$ for all $t$) and both must return to $0$ at step $10$.

---

### 2. Counting 1D Non-Negative Paths (Dyck Paths)
A 1D walk starting at $0$, staying $\ge 0$, and returning to $0$ in $2n$ steps is a classic combinatorial problem solved by **Catalan numbers**.

The number of valid 1D paths of length $2n$ that never drop below 0 and return to 0 is given by the $n$-th Catalan number $C_n$:
$$C_n = \frac{1}{n+1} \binom{2n}{n}$$

For a total of $10$ steps ($n_{total} = 5$ pairs of steps), let $k$ be the number of horizontal steps ($2k$ steps in total, meaning $k$ rights and $k$ lefts), which means there are $5-k$ vertical steps pairs.

---

### 3. Summing Over All Possible Step Distributions
We must sum the product of valid 1D paths for $X$ and $Y$ across all possible allocations of the 5 step-pairs:

$$\text{Total 2D Paths} = \sum_{k=0}^{5} \left( \text{Valid X paths of length } 2k \right) \times \left( \text{Valid Y paths of length } 10-2k \right)$$

Using Catalan numbers $C_m$ for $2m$ steps:
$$\text{Total Paths} = \sum_{k=0}^{5} C_k \cdot C_{5-k}$$

Let's compute each term for $k = 0, 1, 2, 3, 4, 5$:
- $k = 0$: $C_0 \cdot C_5 = 1 \times 42 = 42$
- $k = 1$: $C_1 \cdot C_4 = 1 \times 14 = 14$
- $k = 2$: $C_2 \cdot C_3 = 2 \times 5 = 10$
- $k = 3$: $C_3 \cdot C_2 = 5 \times 2 = 10$
- $k = 4$: $C_4 \cdot C_1 = 14 \times 1 = 14$
- $k = 5$: $C_5 \cdot C_0 = 42 \times 1 = 42$

Summing these up:
$$\text{Total Paths} = 42 + 14 + 10 + 10 + 14 + 42 = \mathbf{132}$$

There are exactly **132 distinct paths** of 10 steps that start and end at $(0,0)$ while never dipping into negative coordinates.

</details>
