# 🟠 12 Balls Puzzle (Unknown Heavy or Light)

## 🎯 Problem Statement
You are given **12 identical-looking balls**.
- Exactly **one ball is counterfeit** and has a different weight.
- **Unknown Information:** You **do not know** whether the fake ball is heavier or lighter than the standard balls.
- You have a classical two-pan balance scale, and you must find the fake ball and determine if it is **heavy or light** in at most **3 weighings**.

### ❓ Question
Can you design a 3-weighing strategy that solves this generalized puzzle without knowing the polarity in advance?

---

<details>
<summary><b>💡 Click to Reveal the Advanced 3-Weighing Matrix Solution</b></summary>

<br>

### 1. The Information Challenge
We need to test 12 balls, and each ball can be either *Heavy* ($H$) or *Light* ($L$). That means there are $12 \times 2 = 24$ possible states. 
With 3 weighings, we have $3^3 = 27$ possible outcome trajectories ($27 \ge 24$), leaving almost no margin for error. Every single outcome must be fully utilized.

---

### 2. Matrix Labeling Strategy
Label the 12 balls from **1 to 12**. 

We divide our weighings using a rigorous balancing matrix where each ball is assigned specific positions (Left, Right, or Unweighed) across the 3 weighings.

#### **Weighing 1:**
* **Left Pan:** Balls `1, 2, 3, 4`
* **Right Pan:** Balls `5, 6, 7, 8`
* **Unweighed (Table):** Balls `9, 10, 11, 12`

#### **Weighing 2 & 3 Setup (Based on Outcome 1):**
Depending on how the first scale tips ($=, <, >$), we shuffle specific subsets into the pans for Weighing 2 and Weighing 3 to isolate the exact ball and its polarity ($H$ or $L$). 

*(Detailed tracking matrix example for Outcome `Left > Right` on Weighing 1):*
* If `1-4 > 5-8`, the fake is either **heavy in {1,2,3,4}** or **light in {5,6,7,8}**.
* We place `1, 2, 5` on the Left pan and `3, 6, 9` on the Right pan for Weighing 2.
* By carefully tracing the 3-step ternary outcome vector (e.g., `>, =, <`), every single one of the 24 possible scenarios maps to a **unique signature**.

---

### 3. Summary Result
By executing this precise multi-permutation weighing matrix, you are guaranteed to:
1. Identify the exact counterfeit ball among the 12.
2. Determine conclusively whether it is **heavier** or **lighter** than the rest in **exactly 3 weighings**.

</details>
