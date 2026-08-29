# 🟠 The Deranged Letters Problem (Derangements)

## 🎯 Problem Statement
You write **$N$ letters** to $N$ different friends and address **$N$ distinct envelopes** with their respective names. 

Due to extreme absent-mindedness, you randomly place the letters into the envelopes without looking (a uniformly random permutation of letters into envelopes).

### ❓ Question
What is the probability that **no letter** ends up in its correct envelope (known mathematically as a **derangement**)? What happens to this probability as $N$ becomes very large?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Inclusion-Exclusion Proof</b></summary>

<br>

### 1. Defining Derangements
A **derangement** is a permutation of elements of a set such that no element appears in its original position. 

Let $D_n$ denote the total number of derangements of $n$ items. The total number of possible permutations for $n$ items is $n!$. Therefore, the probability $P_n$ that a random assignment is a complete derangement is:
$$P_n = \frac{D_n}{n!}$$

---

### 2. The Principle of Inclusion-Exclusion
To count how many permutations leave *no* element in its correct place, we use the Principle of Inclusion-Exclusion (PIE):

1. Start with all possible permutations: $n!$
2. Subtract the permutations where **at least 1** letter is in the correct envelope: $\binom{n}{1}(n-1)!$
3. Add back the permutations where **at least 2** letters are correct (since they were subtracted twice): $\binom{n}{2}(n-2)!$
4. Alternate signs up to $n$ letters.

This gives the exact formula for the number of derangements:
$$D_n = n! - \binom{n}{1}(n-1)! + \binom{n}{2}(n-2)! - \binom{n}{3}(n-3)! + \dots + (-1)^n \binom{n}{n}(0!)$$

Simplifying each binomial term $\binom{n}{k} (n-k)! = \frac{n!}{k!(n-k)!} (n-k)! = \frac{n!}{k!}$:
$$D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!}$$

---

### 3. Probability and the Limit as $N \to \infty$
Dividing $D_n$ by $n!$ gives the exact probability of a random derangement for $n$ letters:
$$P_n = \sum_{k=0}^{n} \frac{(-1)^k}{k!} = 1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \dots + \frac{(-1)^n}{n!}$$

As the number of letters $N$ approaches infinity ($N \to \infty$), this finite sum converges to the Taylor series expansion of $e^{-1}$:
$$\lim_{N \to \infty} P_n = \frac{1}{e} \approx \frac{1}{2.71828} \approx \mathbf{36.787\%}$$

#### Astonishing Insight:
No matter how many letters you have (whether 10, 100, or a billion), the probability that **every single person receives the wrong letter** always hovers right around **$36.8\%$** ($1/e$).

</details>
