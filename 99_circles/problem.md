# 🟠 Maximum Regions Formed by 99 Circles

## 🎯 Problem Statement
Suppose you have **$99$ circles** drawn on a flat two-dimensional plane.

The circles are placed in **general position**, meaning:
1. Every pair of circles intersects at **exactly two distinct points**.
2. **No three circles** intersect at the same common point (no concurrent intersections).
3. No two circles are tangent.

### ❓ Questions
1. What is the **maximum total number of regions** into which the plane is divided by these $99$ circles?
2. How many of these regions are **bounded** (finite area)?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Recurrence Relation</b></summary>

<br>

### 1. Recurrence Formulation
Let $R_n$ denote the maximum number of regions formed by $n$ circles in general position:

- For $n = 0$ circles: $R_0 = 1$ (the entire undivided plane).
- For $n = 1$ circle: $R_1 = 2$ (inside and outside the circle).
- For $n = 2$ intersecting circles: $R_2 = 4$ regions.

When the $n$-th circle is added to an existing configuration of $n-1$ circles:
* It intersects each of the previous $n-1$ circles at at most **$2$ points**.
* The $n$-th circle is therefore intersected at a maximum of:
  $$2(n - 1) \text{ points}$$
* These $2(n - 1)$ intersection points divide the perimeter of the $n$-th circle into **$2(n - 1)$ distinct arcs**.
* Each arc cuts through an existing region and divides it into two, creating **$2(n - 1)$ new regions**.

This gives the recurrence relation:
$$R_n = R_{n-1} + 2(n - 1) \quad \text{for } n \ge 1$$

---

### 2. Closed-Form Formula
Expanding the recurrence:
$$R_n = R_0 + 2\sum_{k=1}^{n-1} k = 1 + 2 \cdot \frac{(n - 1)n}{2}$$

$$R_n = n^2 - n + 2$$

---

### 3. Calculating for $n = 99$ Circles

#### Total Regions:
$$R_{99} = 99^2 - 99 + 2 = 99(99 - 1) + 2 = 99 \times 98 + 2 = 9702 + 2 = \mathbf{9704}$$

#### Bounded vs Unbounded Regions:
* There is only **$1$ unbounded region** (the exterior region extending to infinity).
* The remaining regions are all bounded:
  $$\text{Bounded Regions} = R_{99} - 1 = 9704 - 1 = \mathbf{9703}$$

</details>
