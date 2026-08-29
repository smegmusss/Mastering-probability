# 🟢 Fair Probability from an Unfair Coin

## Problem Statement
If you have an unfair coin, which may bias toward either heads or tails at an unknown probability $p$, can you generate even odds ($50/50$ fair probability) using this coin?

---

## Analytical Solution (Von Neumann's Algorithm)

Unlike fair coins, we cannot generate even odds with a single toss using an unfair coin. Instead, consider tossing the coin in independent pairs $(C_1, C_2)$.

Let:
- $p_H = p$ be the probability of getting Heads ($H$)
- $p_T = 1 - p$ be the probability of getting Tails ($T$)

For two consecutive tosses, there are four possible outcomes:

| Outcome | Probability | Action / Decision |
| :---: | :---: | :---: |
| **$HH$** | $p^2$ | Discard and repeat |
| **$TT$** | $(1 - p)^2$ | Discard and repeat |
| **$HT$** | $p(1 - p)$ | **Win (Fair Outcome 1)** |
| **$TH$** | $(1 - p)p = p(1 - p)$ | **Lose (Fair Outcome 0)** |

### Symmetry Argument
Notice that:
$$P(HT) = P(TH) = p(1 - p)$$

By assigning the outcome $HT$ to a win (or Heads) and $TH$ to a loss (or Tails), and re-tossing whenever $HH$ or $TT$ occurs, we guarantee that the conditional probability of winning given that the game terminates is:

$$P(\text{Win} \mid \text{Termination}) = \frac{P(HT)}{P(HT) + P(TH)} = \frac{p(1 - p)}{2p(1 - p)} = \frac{1}{2}$$

---

## Complexity & Expected Flips

The probability that a pair of tosses results in a decision is:
$$P(\text{Decision}) = P(HT) + P(TH) = 2p(1 - p)$$

The number of pairs required follows a Geometric distribution. Therefore, the expected total number of coin tosses needed to produce one unbiased bit is:

$$\mathbb{E}[\text{Total Flips}] = \frac{2}{2p(1 - p)} = \frac{1}{p(1 - p)}$$
