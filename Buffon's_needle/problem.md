# 🟠 Buffon's Needle Problem (Estimating $\pi$)

## 🎯 Problem Statement
A flat floor is marked with parallel, equidistant lines spaced by a distance $D$.  
A thin needle of length $L$ (where $L \le D$, the "short needle" case) is dropped uniformly at random onto the floor.

### ❓ Questions
1. What is the exact probability $P(\text{Cross})$ that the needle intersects at least one of the parallel lines?
2. How can this physical experiment be used as a Monte Carlo method to approximate $\pi$?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Derivation & Integral Proof</b></summary>

<br>

### 1. Defining the State Space
Let the random position of the needle be parameterized by two independent continuous random variables:

1. **$X \sim \text{Uniform}\left[0, \frac{D}{2}\right]$**: The perpendicular distance from the center of the needle to the nearest parallel line.
2. **$\Theta \sim \text{Uniform}\left[0, \frac{\pi}{2}\right]$**: The acute angle between the needle and the parallel lines.

Because the needle is dropped uniformly at random, the joint probability density function is constant over the domain:
$$f_{X, \Theta}(x, \theta) = f_X(x) \cdot f_\Theta(\theta) = \frac{1}{D/2} \cdot \frac{1}{\pi/2} = \frac{4}{\pi D}$$

$$\text{for } 0 \le x \le \frac{D}{2} \quad \text{and} \quad 0 \le \theta \le \frac{\pi}{2}$$

---

### 2. Geometric Intersection Condition
By simple trigonometry, half of the needle projects onto the perpendicular axis by a length of $\frac{L}{2} \sin \theta$.

The needle crosses a line **if and only if** the distance from its center to the nearest line is less than or equal to this projection:
$$X \le \frac{L}{2} \sin \theta$$

---

### 3. Computing the Probability via Double Integral
We integrate the joint PDF over the region satisfying the condition:

$$P(\text{Cross}) = \int_{0}^{\pi/2} \int_{0}^{\frac{L}{2}\sin\theta} f_{X, \Theta}(x, \theta) \, dx \, d\theta$$

$$P(\text{Cross}) = \frac{4}{\pi D} \int_{0}^{\pi/2} \left[ \int_{0}^{\frac{L}{2}\sin\theta} 1 \, dx \right] d\theta$$

$$P(\text{Cross}) = \frac{4}{\pi D} \int_{0}^{\pi/2} \frac{L}{2} \sin\theta \, d\theta = \frac{2L}{\pi D} [-\cos\theta]_0^{\pi/2}$$

Since $-\cos(\pi/2) - (-\cos(0)) = 0 - (-1) = 1$:

$$P(\text{Cross}) = \frac{2L}{\pi D}$$

---

### 4. Estimating $\pi$ via Monte Carlo
If we perform $N$ random drops and observe $H$ line crossings (hits), the empirical crossing frequency approximates the theoretical probability:

$$\frac{H}{N} \approx \frac{2L}{\pi D} \implies \hat{\pi} \approx \frac{2L \cdot N}{D \cdot H}$$

</details>
