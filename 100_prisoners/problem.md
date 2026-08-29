# 💀 100 Prisoners and 100 Boxes

## 🎯 Problem Statement
A warden offers a challenge to **100 numbered prisoners** (from 1 to 100).

- In a closed room, there are **100 closed boxes**, labeled on the outside from 1 to 100.
- Inside each box is a card with a distinct number from 1 to 100, randomly shuffled (forming a uniform random permutation).
- Each prisoner enters the room one by one and may open at most **50 boxes** to find the card containing their own number.
- After inspecting the boxes, the prisoner must leave the room exactly as they found it.
- **No communication** or mark-leaving is allowed once the process begins (they may only coordinate a strategy beforehand).

### 🏆 Condition for Freedom
**All 100 prisoners must find their own number.** If even a single prisoner fails to find their number, all prisoners are executed.

### ❓ Question
If each prisoner chooses 50 boxes at random, their probability of surviving is negligible:
$$P(\text{Random Guessing}) = \left(\frac{1}{2}\right)^{100} \approx 7.89 \times 10^{-31}$$

Can the prisoners devise a strategy that grants them a significantly higher probability of survival?

---

<details>
<summary><b>💡 Click to Reveal the Strategy & Proof</b></summary>

<br>

### 1. The Naive Strategy (Why Random Guessing Fails)
If each prisoner selects 50 boxes completely at random, each individual has a success probability of $\frac{50}{100} = \frac{1}{2}$.

Because their choices are independent, the joint probability that all 100 prisoners survive is:
$$P(\text{Survival}) = \left(\frac{1}{2}\right)^{100} \approx 7.89 \times 10^{-31} \approx 0$$

---

### 2. The Cycle-Following Strategy (Loop Strategy)
The prisoners agree on the following deterministic procedure:

1. Prisoner $k$ enters the room and opens **Box $k$**.
2. Look at the number inside the box, say $c_1$.
3. If $c_1 = k$, the prisoner has succeeded and stops.
4. If $c_1 \neq k$, the prisoner opens **Box $c_1$**.
5. Continue following the numbers from box to box until finding $k$ or reaching 50 opened boxes.

---

### 3. Mathematical Proof (Permutation Cycles)
Any random placement of numbers in the boxes represents a permutation $\sigma \in S_{100}$. Every permutation decomposes uniquely into a set of disjoint **cycles**.

* When a prisoner follows the chain of numbers, they are simply traversing the cycle containing their number.
* Prisoner $k$ will succeed **if and only if** their cycle length is $\le 50$.
* Therefore, **all 100 prisoners succeed simultaneously if and only if the permutation contains NO cycle of length $> 50$.**

#### Probability of a Cycle of Length $L > 50$:
For any fixed length $L > 50$, there can be at most one cycle of length $L$ in a permutation of 100 elements.

The number of permutations of $n=100$ having a cycle of length $L$ is:
$$\binom{100}{L} \times (L - 1)! \times (100 - L)! = \frac{100!}{L \cdot (100 - L)!} \cdot (100 - L)! = \frac{100!}{L}$$

Dividing by the total number of permutations ($100!$), the probability of having a cycle of length $L$ is simply:
$$P(\text{Cycle of length } L) = \frac{1}{L}$$

Since cycles of length $L > 50$ are mutually exclusive, the total probability that the prisoners **fail** is:
$$P(\text{Failure}) = \sum_{L=51}^{100} \frac{1}{L}$$

Approximating with the harmonic sum integral:
$$\sum_{L=51}^{100} \frac{1}{L} \approx \int_{50}^{100} \frac{1}{x} \, dx = \ln(100) - \ln(50) = \ln(2) \approx 0.6931$$

Thus, the probability of **survival** is:
$$P(\text{Survival}) = 1 - \sum_{L=51}^{100} \frac{1}{L} = 1 - (\ln 2) \approx \mathbf{31.18\%}$$

</details>
