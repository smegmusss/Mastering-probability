# 🟠 Expected Value: Wald's Identity (Random Sum of Random Variables)

## 🎯 Problem Statement
Suppose you visit a casino every day. 
- The number of rounds you play on any given day is a random variable $N$, with an expected value $E[N] = 10$.
- In each round, your profit (or loss) is a random variable $X_i$, where each $X_i$ is independent and identically distributed (i.i.d.) with an expected profit per round of $E[X_i] = \$5$.
- Assume the total number of rounds $N$ is independent of the individual round outcomes $X_i$.

### ❓ Question
What is your expected total profit for the day, defined as $S = \sum_{i=1}^{N} X_i$ (the sum of a random number of random variables)?

---

<details>
<summary><b>💡 Click to Reveal Wald's Identity & The Analytical Solution</b></summary>

<br>

### 1. Wald's Identity Statement
**Wald's Identity** (or Wald's Lemma) is a powerful theorem in probability theory that allows us to find the expected value of the sum of a random number of random variables without needing to know the distribution of the sum itself.

If $N$ is a stopping time (or a random variable independent of the sequence $X_1, X_2, \dots$ with finite mean) and $X_1, X_2, \dots$ are i.i.d. with finite mean, then:
$$E\left[ \sum_{i=1}^{N} X_i \right] = E[N] \cdot E[X]$$

---

### 2. Why Intuition Can Be Tricky
A common mistake is thinking: *"Does the variance or distribution of $N$ change the expected outcome?"* 
- Even if $N$ has a wide spread (sometimes you play 2 rounds, sometimes 50 rounds), Wald's Identity tells us that as long as $N$ and $X_i$ are independent (or $N$ is a proper stopping time), the expected total is simply **the expected number of terms multiplied by the expected value of each term**.

---

### 3. Calculating the Final Answer
Using our problem values:
- Expected number of rounds: $E[N] = 10$
- Expected profit per round: $E[X] = 5$

$$E[S] = E[N] \cdot E[X] = 10 \times 5 = \mathbf{\$50}$$

Your expected total profit for the day is **\$50**.

</details>
