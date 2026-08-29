# 🔴 Hard: Expected Product of Face Counts in 10 Die Rolls (Multinomial Expectation)

## 🎯 Problem Statement
A fair six-sided die is rolled **$10$ times independently**. 
For each face $i \in \{1, 2, 3, 4, 5, 6\}$, let $N_i$ denote the number of times face $i$ appears in the 10 rolls (so that $\sum_{i=1}^{6} N_i = 10$).

### ❓ Question
Compute the expected value of the product of all six counts: 
$$E[N_1 N_2 N_3 N_4 N_5 N_6]$$

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Probability Generating Functions / Multinomial Proof</b></summary>

<br>

### 1. The Trap of Independence
A common mistake is assuming the counts $N_1, N_2, \dots, N_6$ are independent. They are **not independent**, because the total sum is fixed:
$$N_1 + N_2 + N_3 + N_4 + N_5 + N_6 = 10$$
Because of this constraint, if you roll a lot of 1s, there are fewer slots left for the other numbers. Therefore, we cannot simply write $E[N_1]E[N_2]\dots$ as a product of individual expectations.

---

### 2. Using Probability Generating Functions (PGFs) or Indicator Variables
To compute the expectation of a product of random variables whose sum is constrained, the standard advanced tool is either a **Probability Generating Function** or the **factorial moments of a multinomial distribution**.

The distribution of $(N_1, N_2, \dots, N_6)$ is a **multinomial distribution** with parameters $n = 10$ and probabilities $p_1 = p_2 = \dots = p_6 = \frac{1}{6}$.

We want to find the mixed moment:
$$E[N_1 N_2 N_3 N_4 N_5 N_6]$$

---

### 3. Evaluating the Multinomial Expansion
For a multinomial distribution where $n = 10$ and there are $k = 6$ categories:
* The total number of trials is $n = 10$.
* We are asked to find the expected value of the product of all $6$ counts ($N_1 N_2 N_3 N_4 N_5 N_6$).

Notice that the sum of the indices in our product is $1 + 1 + 1 + 1 + 1 + 1 = 6$. 
Since the total number of trials is $n = 10$, and we are multiplying six distinct variables, this corresponds to a specific coefficient in the factorial moments of the multinomial distribution.

Using the property of multinomial factorial moments:
$$E[N_1 N_2 N_3 N_4 N_5 N_6] = \frac{n!}{(n - k)!} \cdot p_1 p_2 p_3 p_4 p_5 p_6$$
*(where $k = 6$ is the number of variables being multiplied).*

Let's plug in our values:
* $n = 10$
* $k = 6$
* $n - k = 10 - 6 = 4$
* Each probability $p_i = \frac{1}{6}$

$$\frac{n!}{(n-6)!} = \frac{10!}{4!} = 10 \times 9 \times 8 \times 7 \times 6 \times 5 = 151,200$$

The product of the probabilities for all 6 faces is:
$$\prod_{i=1}^{6} p_i = \left(\frac{1}{6}\right)^6 = \frac{1}{46,656}$$

---

### 4. Final Calculation
Multiplying the combinatorial term by the probability term:
$$E[N_1 N_2 N_3 N_4 N_5 N_6] = 151,200 \times \frac{1}{46,656}$$

Simplifying the fraction:
- Both numbers are divisible by $7,776$ (or simplify step by step):
  $$\frac{151,200}{46,656} = \frac{3,150}{972} = \frac{1,750}{540} = \frac{175}{54} \approx \mathbf{3.2407}$$

Exact fraction value:
$$E[N_1 N_2 N_3 N_4 N_5 N_6] = \mathbf{\frac{175}{54}}$$

</details>
