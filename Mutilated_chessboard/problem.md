# 🟢 The Mutilated Chessboard Problem

## 🎯 Problem Statement
Consider a standard $8 \times 8$ chessboard consisting of $64$ alternating black and white squares.

- Two squares located at **opposite diagonally corners** of the board are removed (leaving $62$ squares in total).
- You are given **$31$ domino tiles**, where each domino tile has the exact size of $2 \times 1$ squares (covering exactly $2$ adjacent squares on the board).

### ❓ Question
Is it possible to completely cover all the remaining $62$ squares on the board using the $31$ domino tiles without any overlaps or hanging edges? Prove your answer.

---

<details>
<summary><b>💡 Click to Reveal the Analytical Proof</b></summary>

<br>

### 1. The Color Invariant
A standard $8 \times 8$ chessboard has:
- $32$ White squares
- $32$ Black squares

Any domino of size $2 \times 1$ placed horizontally or vertically on the board **must always cover exactly one white square and one black square**, regardless of where or how it is placed.

Therefore, any collection of $31$ non-overlapping dominoes must cover:
$$\text{Squares Covered} = 31 \text{ White squares} + 31 \text{ Black squares}$$

---

### 2. Parity of the Mutilated Board
On a standard chessboard, two diagonally opposite corners **always share the exact same color** (either both are white, or both are black).

When two diagonally opposite corner squares are removed:
- If two white corners are removed, the remaining board has **$30$ White squares and $32$ Black squares**.
- If two black corners are removed, the remaining board has **$32$ White squares and $30$ Black squares**.

In either case:
$$\text{Number of White squares} \neq \text{Number of Black squares}$$

---

### 3. Conclusion
Because every set of $31$ dominoes strictly requires an equal number of black and white squares ($31$ each), but the mutilated board has an unequal distribution ($30$ vs $32$):

**It is mathematically impossible** to cover the mutilated chessboard with $31$ domino tiles.

</details>
