# 🟢 Simulating a Fair Coin with an Unfair One

## 🎯 Problem Statement
You are given a physical coin that is biased: the probability $p$ of landing on **Heads** is strictly between $0$ and $1$ ($p \neq 0.5$), but the exact value of $p$ is unknown to you.

Design an algorithm using only this biased coin to simulate a perfectly fair **50/50** decision.

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution</b></summary>

<br>

### The Core Symmetry Insight
Flip the biased coin in independent consecutive pairs $(C_1, C_2)$:

- $P(HT) = p(1 - p)$
- $P(TH) = (1 - p)p = p(1 - p)$
- $P(HH) = p^2$
- $P(TT) = (1 - p)^2$

Since $P(HT) = P(TH)$:
1. If the outcome is **$HT$**, declare **Heads (1)**.
2. If the outcome is **$TH$**, declare **Tails (0)**.
3. If $HH$ or $TT$ occurs, discard both and repeat.

### Expected Flips
$$\mathbb{E}[\text{Total Flips}] = \frac{1}{p(1 - p)}$$

</details>
