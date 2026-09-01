# 🟠 Optimal Stopping: 3-Dice Roll Game

## 🎯 Problem Statement
You are offered a game where you may roll a fair six-sided die up to **3 times**.
* After each roll, you have two choices:
  1. **Stop** and collect the face value of the die in dollars.
  2. **Roll again**, forfeiting the current roll's value.
* If you reach the **3rd roll**, you must accept whatever value appears.

### ❓ Question
Assuming optimal play at each step, what is the expected payout in dollars?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Backward Induction</b></summary>

<br>

### 1. Roll 3 (Terminal State)
On the 3rd roll, there are no further choices. The expected value is simply the standard expectation of a fair 6-sided die:
$$\mathbb{E}[R_3] = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = \mathbf{3.5\$}$$

---

### 2. Roll 2 Decision
At Roll 2, you compare the visible roll value $x_2$ against the expected return of continuing ($\mathbb{E}[R_3] = 3.5\$$):
* **Stop** if $x_2 > 3.5 \implies x_2 \in \{4, 5, 6\}$ (probability $\frac{3}{6} = \frac{1}{2}$).
* **Reroll** if $x_2 < 3.5 \implies x_2 \in \{1, 2, 3\}$ (probability $\frac{3}{6} = \frac{1}{2}$).

Using the Law of Total Expectation:
$$\mathbb{E}[R_2] = P(\text{Stop}) \cdot \mathbb{E}[R_2 \mid \text{Stop}] + P(\text{Reroll}) \cdot \mathbb{E}[R_3]$$

$$\mathbb{E}[R_2] = \left(\frac{1}{2} \times \frac{4 + 5 + 6}{3}\right) + \left(\frac{1}{2} \times 3.5\right)$$

$$\mathbb{E}[R_2] = \left(\frac{1}{2} \times 5\right) + \left(\frac{1}{2} \times 3.5\right) = 2.5 + 1.75 = \mathbf{4.25\$} \quad \left(\frac{17}{4}\$\right)$$

---

### 3. Roll 1 Decision & Expected Game Payout
At Roll 1, you compare the visible roll value $x_1$ against the expected return of continuing ($\mathbb{E}[R_2] = 4.25\$$):
* **Stop** if $x_1 > 4.25 \implies x_1 \in \{5, 6\}$ (probability $\frac{2}{6} = \frac{1}{3}$).
* **Reroll** if $x_1 < 4.25 \implies x_1 \in \{1, 2, 3, 4\}$ (probability $\frac{4}{6} = \frac{2}{3}$).

Calculating the overall expected payout:
$$\mathbb{E}[\text{Game}] = P(\text{Stop}) \cdot \mathbb{E}[R_1 \mid \text{Stop}] + P(\text{Reroll}) \cdot \mathbb{E}[R_2]$$

$$\mathbb{E}[\text{Game}] = \left(\frac{1}{3} \times \frac{5 + 6}{2}\right) + \left(\frac{2}{3} \times \frac{17}{4}\right)$$

$$\mathbb{E}[\text{Game}] = \left(\frac{1}{3} \times 5.5\right) + \left(\frac{17}{6}\right) = \frac{11}{6} + \frac{17}{6} = \frac{28}{6} = \mathbf{\frac{14}{3}\$}$$

Converting to a decimal:
$$\frac{14}{3}\$ \approx \mathbf{4.67\$} \quad (\mathbf{4.666\dots\$})$$

---

### Optimal Strategy Summary
* **Roll 1:** Stop on **5 or 6**; otherwise reroll.
* **Roll 2:** Stop on **4, 5, or 6**; otherwise reroll.
* **Roll 3:** Accept the final outcome.

</details>
