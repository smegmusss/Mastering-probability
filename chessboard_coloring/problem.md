# 🟢 Grid Parity & Neighbors Conflict Resolution (Chessboard Coloring)

## 🎯 Problem Statement
You are given an **$m \times n$ grid** of arbitrary integers. 
- Two cells are defined as **neighbors** if they share a common side (horizontal or vertical, 4-connectivity).
- You are allowed to modify each cell independently by increasing its value by **at most 1** (i.e., you can either leave a cell unchanged $+0$ or increment it by $+1$).

### ❓ Question
Is it always possible to modify **any arbitrary grid** such that **no cell shares the same value with any of its neighbors**? 
- If yes, provide a universal algorithm/rule that guarantees this condition.
- If not, provide a counterexample grid where this transformation is impossible.

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Chessboard Parity Proof</b></summary>

<br>

### 1. The Core Verdict: It is ALWAYS Possible
Regardless of the dimensions $m \times n$ or the initial distribution of numbers in the grid, it is **always possible** to achieve this configuration using a deterministic, single-pass algorithm based on **bipartite graph coloring (chessboard coloring)** and **integer parity**.

---

### 2. The Chessboard Coloring Insight
Any 2D grid graph is **bipartite**:
- Assign each cell $(i, j)$ a color based on the parity of its coordinates:
  - **Black cells:** cells where $(i + j)$ is **even**.
  - **White cells:** cells where $(i + j)$ is **odd**.

Because cells only share edges with orthogonally adjacent neighbors:
* Every neighbor of a **Black cell** is strictly a **White cell**.
* Every neighbor of a **White cell** is strictly a **Black cell**.

---

### 3. The Parity Assignment Strategy
Two integers can never be equal if one is **even** and the other is **odd**. 

Therefore, if we enforce that:
1. **All Black cells** have **EVEN** numbers, and
2. **All White cells** have **ODD** numbers,

then **no two adjacent cells can ever have the same value**, because an even integer can never equal an odd integer!

---

### 4. The Construction (Adding $\le 1$ to Each Cell)
For every cell $(i, j)$ with initial value $A_{i,j}$:

* **If $(i + j)$ is Even (Black cell):** We want the final value to be **EVEN**.
  - If $A_{i,j}$ is already even $\to$ add **$0$**.
  - If $A_{i,j}$ is odd $\to$ add **$+1$** (making it even).

* **If $(i + j)$ is Odd (White cell):** We want the final value to be **ODD**.
  - If $A_{i,j}$ is already odd $\to$ add **$0$**.
  - If $A_{i,j}$ is even $\to$ add **$+1$** (making it odd).

### Conclusion
Since every modification adds either $0$ or $1$, the condition "increased by at most 1" is strictly respected for every cell, guaranteeing a valid solution for any input grid in $O(m \times n)$ time.

</details>
