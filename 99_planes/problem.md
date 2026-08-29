# 🔴 Space Partitioning by 99 Planes

## 🎯 Problem Statement
Suppose you have **$99$ flat planes** in three-dimensional Euclidean space ($\mathbb{R}^3$).

The planes are in **general position**, meaning:
1. No two planes are parallel (every pair of planes intersects in a straight line).
2. No three planes are parallel to the same line, and any three planes intersect at **exactly one unique point**.
3. **No four planes** intersect at the same common point.

### ❓ Question
What is the **maximum number of 3D regions (cells)** into which the space is divided by these $99$ planes?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Dimension-Ladder Proof</b></summary>

<br>

### 1. Dimensional Recurrence Principle
Let:
- $L_n$ be the maximum number of segments dividing a 1D line with $n$ points.
- $P_n$ be the maximum number of 2D regions dividing a flat plane with $n$ lines.
- $S_n$ be the maximum number of 3D cells dividing 3D space with $n$ planes.

When adding the $n$-th plane into a 3D space with $n-1$ existing planes:
1. The $n$-th plane is intersected by each of the previous $n-1$ planes, creating **$n-1$ straight lines on its 2D surface**.
2. Because the planes are in general position, these $n-1$ lines on the new plane are also in general position in 2D.
3. These $n-1$ lines partition the $n$-th plane into **$P_{n-1}$ two-dimensional regions**.
4. Each 2D region on the new plane slices an existing 3D cell into two new cells, adding exactly $P_{n-1}$ new 3D regions.

This establishes the fundamental dimension-ladder recurrence:
$$S_n = S_{n-1} + P_{n-1}$$

---

### 2. Deriving the 2D Line Formula ($P_n$)
For 2D lines dividing a plane:
* Each new line is cut by $k-1$ existing lines into $k$ segments (1D regions).
* $P_k = P_{k-1} + k$ with $P_0 = 1$.
* Solving the sum:
  $$P_n = 1 + \sum_{k=1}^n k = 1 + \frac{n(n+1)}{2} = \binom{n}{0} + \binom{n}{1} + \binom{n}{2}$$

---

### 3. Deriving the 3D Plane Closed-Form ($S_n$)
Using the recurrence $S_n = S_{n-1} + P_{n-1}$ with base case $S_0 = 1$:

$$S_n = 1 + \sum_{k=0}^{n-1} P_k = 1 + \sum_{k=0}^{n-1} \left(1 + \frac{k(k+1)}{2}\right)$$

Using binomial identities (the "Hockey-Stick" identity):
$$S_n = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} + \binom{n}{3}$$

Expanding the binomial coefficients:
$$S_n = 1 + n + \frac{n(n-1)}{2} + \frac{n(n-1)(n-2)}{6} = \frac{n^3 + 5n + 6}{6}$$

---

### 4. Calculation for $n = 99$ Planes

$$S_{99} = \binom{99}{0} + \binom{99}{1} + \binom{99}{2} + \binom{99}{3}$$

- $\binom{99}{0} = 1$
- $\binom{99}{1} = 99$
- $\binom{99}{2} = \frac{99 \times 98}{2} = 4851$
- $\binom{99}{3} = \frac{99 \times 98 \times 97}{6} = 33 \times 49 \times 97 = 156849$

Summing all terms:
$$S_{99} = 1 + 99 + 4851 + 156849 = \mathbf{161800}$$

</details>
