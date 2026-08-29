# 🟢 Poisoned Wine Bottles and the 10 Servants

## 🎯 Problem Statement
A royal palace has **$1000$ bottles of wine**, but the king learns that exactly **one bottle contains a deadly, undetectable poison**.

- Even a single drop of the poisoned wine is fatal.
- The poison takes **24 hours** to take effect (a servant dies exactly 24 hours after tasting).
- You have **$10$ royal servants (or tasters)** at your disposal.
- The royal banquet starts in exactly **24 hours**, meaning you can only run **one single round of simultaneous tasting**.

### ❓ Question
How can you determine with 100% certainty which specific bottle is poisoned within the 24-hour time limit?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Comparison</b></summary>

<br>

### 1. The Combinatorial "Brute Force" Approach (And Why It's Impractical)
It is theoretically possible to frame this as an exact combinatorial assignment problem:

* If each servant drinks from an arbitrary subset of bottles, you want every bottle to be tasted by a **unique combination of servants**.
* The number of ways to assign subsets of servants is governed by the binomial expansion:
  $$\sum_{k=0}^{10} \binom{10}{k} = \binom{10}{0} + \binom{10}{1} + \binom{10}{2} + \dots + \binom{10}{10} = 2^{10} = 1024$$
* In a brute-force approach, one might try to manually partition the $1000$ bottles into:
  - $\binom{10}{1} = 10$ bottles tasted by exactly 1 servant,
  - $\binom{10}{2} = 45$ bottles tasted by pairs of servants,
  - $\binom{10}{3} = 120$ bottles tasted by triplets,
  - $\binom{10}{4} = 210$, $\binom{10}{5} = 252$, and so forth.

**The downside:** Trying to manually track, mix, and cross-reference which subset of servants drank from which bottle without a systematic scheme requires tedious combinatorial calculations, table lookups, and is prone to human error under interview pressure.

---

### 2. The Information Theory & Binary Approach (Optimal)
Instead of arbitrary combinatorial mapping, we use **Base-2 (Binary) representation**, which gives a 1-to-1 deterministic encoding with zero calculations.

#### Information Capacity:
Each servant has two possible states after 24 hours:
- $\text{Alive} \to 0$
- $\text{Dead} \to 1$

With $10$ servants, there are $2^{10} = 1024$ distinct joint states. Since $1024 \ge 1000$, $10$ bits of information are strictly sufficient to isolate the single poisoned bottle.

---

### 3. Step-by-Step Binary Strategy

1. **Number the bottles** in decimal from $1$ to $1000$, and write their 10-bit binary representation:
   - $\text{Bottle } 1 = 0000000001_2$
   - $\text{Bottle } 2 = 0000000010_2$
   - $\text{Bottle } 3 = 0000000011_2$
   - $\dots$
   - $\text{Bottle } 1000 = 1111101000_2$

2. **Assign each servant to a bit index:**
   - Servant $0 \to$ Bit $0$ ($2^0 = 1$)
   - Servant $1 \to$ Bit $1$ ($2^1 = 2$)
   - Servant $2 \to$ Bit $2$ ($2^2 = 4$)
   - $\dots$
   - Servant $9 \to$ Bit $9$ ($2^9 = 512$)

3. **Mixing the samples:**  
   Servant $k$ takes a sip from bottle $B$ **if and only if** the $k$-th bit of $B$ in binary is **$1$**.

---

### 4. Reading the Result After 24 Hours
After 24 hours, line up the servants from index $9$ down to index $0$:
- If Servant $k$ dies, write a **$1$** at position $k$.
- If Servant $k$ survives, write a **$0$** at position $k$.

The resulting 10-bit binary string is the exact decimal index of the poisoned bottle.

#### Example:
Suppose **Bottle $105$** is poisoned:
$$105 = 64 + 32 + 8 + 1 = 2^6 + 2^5 + 2^3 + 2^0 = 0001101001_2$$

* Only **Servants 0, 3, 5, and 6** drank from Bottle $105$.
* Exactly Servants 0, 3, 5, and 6 die.
* Reading the binary bits $0001101001_2$ immediately reveals **$105$** without checking any combination table.

</details>
