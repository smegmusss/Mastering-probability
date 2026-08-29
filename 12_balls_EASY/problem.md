# 🟢 12 Balls Puzzle (Known Heavy / Light)

## 🎯 Problem Statement
You are given **12 identical-looking balls**.
- Exactly **one ball is counterfeit** and its weight differs from the other 11 standard balls.
- **Known Information:** You are told in advance whether the fake ball is **heavier** than the standard balls.
- You have a classical **two-pan balance scale** (no weights, yielding: Left < Right, Left = Right, or Left > Right).

### ❓ Question
What is the minimum number of weighings required to guarantee finding the fake ball, and what is the optimal strategy?

---

<details>
<summary><b>💡 Click to Reveal the 3-Weighing Solution & Decision Tree</b></summary>

<br>

### 1. Information Theory Bound
Each weighing gives 3 possible outcomes ($<, =, >$). With $k$ weighings, you can distinguish at most $3^k$ states.
- For $1$ weighing: $3^1 = 3$ states.
- For $2$ weighings: $3^2 = 9$ states.
- For $3$ weighings: $3^3 = 27$ states.

Since $27 \ge 12$, **3 weighings** are mathematically sufficient.

---

### 2. The Optimal Ternary Partition Strategy

Divide the 12 balls into 3 groups of 4: **Group A (4 balls)**, **Group B (4 balls)**, and **Group C (4 balls)**.

#### **Weighing 1:** Weigh A vs B ($4$ vs $4$)
* **Case 1: Left ($A$) = Right ($B$)**
  * The fake heavier ball must be in **Group C** (the unweighed group of 4).
  * *Weighing 2:* Take 2 balls from C and weigh them ($1$ vs $1$).
    * If equal $\to$ the fake is one of the remaining 2 in C. *Weighing 3:* weigh 1 vs 1 to find it.
    * If unequal $\to$ the heavier one is identified immediately.
  * *Total weighings used:* **3 weighings max**.

* **Case 2: Left ($A$) $\neq$ Right ($B$)**
  * Since we know the fake ball is **heavier**, whichever side is heavier on the scale contains the fake ball. We narrow our suspect list from 12 down to **4 balls**.
  * *Weighing 2:* Take those 4 suspect balls and split them into pairs ($2$ vs $2$). Weigh them.
    * The heavier side gives us **2 suspect balls**.
  * *Weighing 3:* Take those final 2 balls and weigh them ($1$ vs $1$). The heavier one is the fake ball.
  * *Total weighings used:* **3 weighings**.

</details>
