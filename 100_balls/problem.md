# 🟢 The 50 White & 50 Black Balls Optimization

## 🎯 Problem Statement
You are given **50 white balls** and **50 black balls** (total of 100 balls) and **two identical empty boxes**.

### ❓ Question
How should you distribute all 100 balls between the two boxes to **maximize the probability** that, if you choose a box uniformly at random ($50\%$ chance for each) and then draw a single ball uniformly at random from that chosen box, **the drawn ball is white**?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & The Counter-Intuitive Split</b></summary>

<br>

### 1. Why a Balanced Split Fails
A common intuition is to split everything evenly (e.g., 25 white and 25 black in each box). 

If you do this, the probability of drawing a white ball from either box is always $\frac{25}{50} = \frac{1}{2}$, making the total probability:
$$P(W) = \frac{1}{2}\left(\frac{1}{2}\right) + \frac{1}{2}\left(\frac{1}{2}\right) = \mathbf{50\%}$$

Can we do significantly better? Yes, by leveraging asymmetry.

---

### 2. The Optimal Configuration Strategy
To maximize the chance of picking a white ball, we want to guarantee a $100\%$ success rate for *at least one* box, while packing as many remaining white balls as possible into the second box to keep its ratio high.

* **Box 1:** Put **1 white ball** and **0 black balls**.
  - Probability of drawing white if Box 1 is chosen: $\frac{1}{1} = 1.0$ ($100\%$).
* **Box 2:** Put the remaining **49 white balls** and **50 black balls**.
  - Probability of drawing white if Box 2 is chosen: $\frac{49}{49 + 50} = \frac{49}{99}$.

---

### 3. Calculating the Maximum Total Probability
Using the Law of Total Probability:
$$P(W) = P(\text{Box 1}) \cdot P(W \mid \text{Box 1}) + P(\text{Box 2}) \cdot P(W \mid \text{Box 2})$$

$$P(W) = \frac{1}{2}(1) + \frac{1}{2}\left(\frac{49}{99}\right)$$

$$P(W) = \frac{1}{2} + \frac{49}{198} = \frac{99}{198} + \frac{49}{198} = \frac{148}{198} = \frac{74}{99}$$

Converting to a decimal/percentage:
$$\frac{74}{99} \approx \mathbf{0.7475} \quad (\mathbf{74.75\% \text{ or roughly } 3/4})$$

By isolating a single white ball in one box, you boost your success rate from a flat $50\%$ up to nearly $75\%$.

</details>
