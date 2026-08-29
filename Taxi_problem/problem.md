# 🟠 The Taxi Accident Probability Problem (Poisson Process)

## 🎯 Problem Statement
The probability of observing **at least one traffic accident** on a specific highway stretch during any given 1-hour time window is **$10\%$ ($0.10$)**. 

Assuming that accidents occur independently and follow a continuous-time stochastic process with a constant rate over time:

### ❓ Question
What is the probability of observing **at least one accident** during a larger time window of **$2$ hours**?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Pitfall Warning</b></summary>

<br>

### 1. The Common Intuition Trap (Why 20% is WRONG)
A naive approach is to assume proportionality:
$$\text{If 1 hour} = 10\%, \text{ then 2 hours} = 2 \times 10\% = 20\%$$

**Why this is incorrect:** Probabilities cannot simply be added together across independent time intervals because if you extended this logic to 20 hours, you would get $200\%$ ($2.0$), which is mathematically impossible for a probability.

---

### 2. The Correct Mathematical Approach (Poisson Process)
Let $X(t)$ be the number of accidents in $t$ hours. The arrival of accidents follows a **Poisson Process** with rate parameter $\lambda$ per hour.

The probability of observing **zero accidents** in a time interval of length $t$ is given by the Poisson distribution formula:
$$P(X(t) = 0) = e^{-\lambda t}$$

#### Step 1: Find the rate $\lambda$
We are given that the probability of at least one accident in $1$ hour ($t = 1$) is $0.10$:
$$P(X(1) \ge 1) = 0.10$$

Since the probability of at least one accident is the complement of zero accidents:
$$1 - P(X(1) = 0) = 0.10 \implies P(X(1) = 0) = 0.90$$

Using the Poisson formula for $t = 1$:
$$e^{-\lambda (1)} = 0.90 \implies \lambda = -\ln(0.90) \approx 0.10536$$

---

#### Step 2: Compute for a 2-Hour Window ($t = 2$)
We want to find the probability of **at least one accident** in 2 hours ($t = 2$):
$$P(X(2) \ge 1) = 1 - P(X(2) = 0)$$

Using our rate $\lambda$ for $t = 2$:
$$P(X(2) = 0) = e^{-\lambda (2)} = \left(e^{-\lambda}\right)^2 = (0.90)^2 = 0.81$$

Therefore, the probability of at least one accident in 2 hours is:
$$P(X(2) \ge 1) = 1 - 0.81 = \mathbf{0.19} \quad (\mathbf{19\%})$$

*(Notice that $19\%$ is slightly less than the naive guess of $20\%$ due to the non-linear compounding nature of exponential decay / Poisson arrivals).*

</details>
