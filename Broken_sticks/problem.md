# 🔴 The Broken Stick Triangle Paradox

## 🎯 Problem Statement
A straight stick of length $L$ is broken into **three pieces** at two points chosen **uniformly and independently at random** along its length.

### ❓ Question
What is the exact probability that the three resulting pieces can form a **non-degenerate triangle** (i.e., the sum of the lengths of any two pieces is strictly greater than the length of the third piece)?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Geometric Simplex Proof</b></summary>

<br>

### 1. The Geometric Setup
Let the length of the stick be $1$. We choose two random break points, $X$ and $Y$, uniformly and independently distributed in the interval $[0, 1]$. 

To make our equations simpler, let's assume without loss of generality that $X \le Y$. 
The three pieces formed by these cuts have lengths:
- $a = X$
- $b = Y - X$
- $c = 1 - Y$

Notice that the sum of the three lengths is always $a + b + c = 1$.

---

### 2. The Triangle Inequality Conditions
For three segments of lengths $a, b,$ and $c$ to form a triangle, they must satisfy the **triangle inequalities**:
1. $a + b > c \implies X + (Y - X) > 1 - Y \implies 2Y > 1 \implies Y > \frac{1}{2}$
2. $a + c > b \implies X + (1 - Y) > Y - X \implies 2X - 2Y > -1 \implies Y - X < \frac{1}{2}$
3. $b + c > a \implies (Y - X) + (1 - Y) > X \implies 1 - 2X > 0 \implies X < \frac{1}{2}$

Combining these three conditions, a triangle can be formed if and only if:
- $X < \frac{1}{2}$
- $Y > \frac{1}{2}$
- $Y - X < \frac{1}{2}$ (or equivalently, $X > Y - \frac{1}{2}$)

---

### 3. Visualizing on the Unit Square
If we plot $X$ on the horizontal axis and $Y$ on the vertical axis (with $0 \le X \le Y \le 1$), the sample space of all possible cuts forms a **right-angled isosceles triangle** with an area of $\frac{1}{2}$ (half of a $1 \times 1$ square).

* The successful region where all three triangle inequalities hold forms a smaller central sub-triangle.
* The area of this successful sub-triangle is exactly $\frac{1}{8}$ of the full square (or $\frac{1}{4}$ of the sample space).

Dividing the successful area by the total sample space area:
$$P(\text{Triangle}) = \frac{1/8}{1/2} = \mathbf{\frac{1}{4}} \quad (\mathbf{25\%})$$

The probability that three randomly broken pieces of a stick can form a triangle is exactly **25%**.

</details>
