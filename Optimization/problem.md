# 🟠 Dice Optimization: Maximizing Exactly One Six

## 🎯 Problem Statement
You are rolling a set of $n$ independent, fair six-sided dice simultaneously.

### ❓ Question
How many dice ($n$) should you roll to **maximize the probability of observing exactly one 6**?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Discrete Optimization</b></summary>

<br>

### 1. Binomial Probability Formulation
The number of sixes obtained when rolling $n$ independent fair six-sided dice follows a Binomial distribution:
$$X \sim \text{Binomial}\left(n, \, p = \frac{1}{6}\right)$$

The probability of rolling **exactly one 6** with $n$ dice is given by:
$$P(n) = \binom{n}{1} p^1 (1-p)^{n-1} = n \cdot \left(\frac{1}{6}\right) \cdot \left(\frac{5}{6}\right)^{n-1}$$

---

### 2. Finding the Optimal $n$ via Ratio Test
Since $n$ is an integer, we analyze the ratio between consecutive terms $\frac{P(n+1)}{P(n)}$ to determine where the sequence stops increasing:

$$\frac{P(n+1)}{P(n)} = \frac{(n+1) \cdot \left(\frac{1}{6}\right) \cdot \left(\frac{5}{6}\right)^n}{n \cdot \left(\frac{1}{6}\right) \cdot \left(\frac{5}{6}\right)^{n-1}} = \frac{n+1}{n} \cdot \frac{5}{6}$$

The sequence increases as long as $\frac{P(n+1)}{P(n)} \ge 1$:

$$\frac{n+1}{n} \cdot \frac{5}{6} \ge 1$$

$$5(n+1) \ge 6n$$

$$5n + 5 \ge 6n \implies \mathbf{n \le 5}$$

---

### 3. Comparing the Maximum Points
Evaluating the boundary cases:
* For $n < 5$: $P(n+1) > P(n)$ (strictly increasing).
* For $n = 5$:
  $$\frac{P(6)}{P(5)} = \frac{5+1}{5} \cdot \frac{5}{6} = \frac{6}{5} \cdot \frac{5}{6} = \mathbf{1} \implies P(6) = P(5)$$
* For $n > 5$: $P(n+1) < P(n)$ (strictly decreasing).

Let's compute the exact probability for $n = 5$ and $n = 6$:

$$P(5) = 5 \cdot \left(\frac{1}{6}\right) \cdot \left(\frac{5}{6}\right)^4 = \frac{5^5}{6^5} = \frac{3125}{7776} \approx \mathbf{40.19\%}$$

$$P(6) = 6 \cdot \left(\frac{1}{6}\right) \cdot \left(\frac{5}{6}\right)^5 = \left(\frac{5}{6}\right)^5 = \frac{3125}{7776} \approx \mathbf{40.19\%}$$

---

### Optimal Choice Summary
Rolling either **5 dice** or **6 dice** achieves the exact same maximum probability of obtaining exactly one 6:

$$\mathbf{n = 5 \quad \text{or} \quad n = 6} \qquad \left(P_{\max} = \frac{3125}{7776} \approx \text{40.19\%}\right)$$

</details>
