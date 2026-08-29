# 🟠 Optiver Quant: Sum of 3 Uniform Random Numbers Greater Than 100

## 🎯 Problem Statement
You choose **three numbers** $X, Y, Z$ independently and uniformly at random from the interval $[0, 50]$:
$$X, Y, Z \sim \text{Uniform}(0, 50)$$

### ❓ Question
What is the probability that their sum is **greater than 100** ($X + Y + Z > 100$)?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Geometric Volume Proof</b></summary>

<br>

### 1. Scaling the Sample Space
To make the integration cleaner, let's scale our variables. Since each variable is chosen from $[0, 50]$, let's define normalized variables $u, v, w \in [0, 1]$ such that:
$$X = 50u, \quad Y = 50v, \quad Z = 50w$$

The condition $X + Y + Z > 100$ becomes:
$$50u + 50v + 50w > 100 \implies u + v + w > 2$$

The sample space is a cube of side length $1$ in the $uvw$-space, with a total volume of $V_{\text{total}} = 1^3 = 1$.

---

### 2. Geometric Interpretation
We want to find the fraction of the unit cube where the sum of coordinates $u + v + w$ is **greater than 2**. 

Instead of integrating over the complex region where $u + v + w > 2$, it is much easier to find the volume of the **complementary region** where the sum is **less than or equal to 2** ($u + v + w \le 2$).

The region $u + v + w \le 2$ inside the unit cube $[0,1]^3$ forms a truncated cube. Specifically, the corner where $u=1, v=1, w=1$ is "cut off" by the plane $u + v + w = 2$.

---

### 3. Calculating the Volume of the Cut-Off Corner
The cut-off corner is a small tetrahedron whose vertices are:
- $(1, 1, 1)$
- $(1, 1, 0)$
- $(1, 0, 1)$
- $(0, 1, 1)$

The side lengths of this right-angled tetrahedron along the axes are each equal to $1$ (since the plane intersects the edges at $u=1, v=1, w=1$).

The volume of a right-angled tetrahedron with legs of length $h_1, h_2, h_3$ is:
$$V_{\text{tetrahedron}} = \frac{1}{6} \cdot h_1 \cdot h_2 \cdot h_3 = \frac{1}{6} (1)(1)(1) = \frac{1}{6}$$

---

### 4. Computing the Final Probability
Since the total volume of the unit cube is $1$, the probability that the sum is $\le 2$ is simply the volume of the remainder:
$$P(u + v + w \le 2) = 1 - V_{\text{tetrahedron}} = 1 - \frac{1}{6} = \frac{5}{6}$$

Therefore, the probability that their sum is **greater than 2** (meaning the original sum $X + Y + Z > 100$) is the complement:
$$P(u + v + w > 2) = 1 - \frac{5}{6} = \mathbf{\frac{1}{6}} \quad (\approx \mathbf{16.67\%})$$

</details>
