# 🟠 The 1D Random Walk (Gambler's Ruin / Return to Origin)

## 🎯 Problem Statement
A particle (or a gambler) starts at the origin $0$ on a one-dimensional integer grid ($\mathbb{Z}$). 

At each discrete time step, the particle moves:
- **$+1$** (right) with probability $p$
- **$-1$** (left) with probability $q = 1 - p$

Assume standard **symmetric random walk** where $p = q = 0.5$.

### ❓ Questions
1. If the particle starts at $0$ and moves for $2N$ steps, what is the probability that it returns to the origin at step $2N$?
2. Is the 1D random walk **recurrent** (does it visit the origin infinitely many times with probability 1)?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Proofs</b></summary>

<br>

### 1. Probability of Returning to the Origin at Step $2N$
To return to the origin after $2N$ steps, the particle must take exactly $N$ steps to the right and $N$ steps to the left (total displacement = $0$).

* The total number of possible paths of length $2N$ is $2^{2N}$.
* The number of paths with exactly $N$ rights and $N$ lefts is given by the binomial coefficient $\binom{2N}{N}$.

Thus, the probability $P_{2N}$ of being back at the origin at step $2N$ is:
$$P_{2N} = \frac{\binom{2N}{N}}{2^{2N}} = \frac{(2N)!}{(N!)^2 2^{2N}}$$

#### Using Stirling's Approximation ($n! \approx \sqrt{2\pi n} \left(\frac{n}{e}\right)^n$):
For large $N$:
$$P_{2N} \approx \frac{1}{\sqrt{\pi N}}$$

This means the probability of returning to the origin decreases as $O\left(\frac{1}{\sqrt{N}}\right)$.

---

### 2. Recurrence vs. Transience (Pólya's Random Walk Theorem)
A fundamental question in Markov chains is whether a random walk starting at $0$ will eventually return to $0$ with probability $1$.

Let $f$ be the probability of ever returning to the origin. The expected number of visits to the origin $E[V]$ can be expressed as a geometric sum of return probabilities, or directly via the indicator sum of return probabilities at step $2N$:
$$E[V] = \sum_{N=1}^{\infty} P_{2N} = \sum_{N=1}^{\infty} \frac{\binom{2N}{N}}{2^{2N}}$$

Using the asymptotic approximation $\frac{1}{\sqrt{\pi N}}$:
$$\sum_{N=1}^{\infty} \frac{1}{\sqrt{\pi N}} = \frac{1}{\sqrt{\pi}} \sum_{N=1}^{\infty} N^{-1/2}$$

Since this is a p-series with $p = \frac{1}{2} \le 1$, the sum **diverges to infinity**. 

- Because the expected number of visits is infinite, the probability of return must be $1$.
- **Conclusion:** The 1D symmetric random walk is **recurrent** (the particle is guaranteed to return to the origin infinitely many times if it walks forever). *Note: This property holds true in 2D as well, but breaks in 3D and above (Pólya's Theorem).*

</details>
