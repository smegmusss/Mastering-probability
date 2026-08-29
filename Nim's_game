# 🟠 Classic Multi-Pile Nim (Bouton's Game)

## 🎯 Problem Statement
Two players, **Player A** and **Player B**, play a mathematical game with **$k$ piles of stones**, where the sizes of the piles are $(x_1, x_2, \dots, x_k)$.

- Player A moves first.
- On their turn, a player chooses **one single pile** and removes **any positive number of stones** from that pile (they can take 1 stone, several stones, or the entire pile).
- **Normal Play Rule:** The player who takes the **very last stone** wins the game.

### ❓ Question
Given an arbitrary initial configuration of pile sizes $(x_1, x_2, \dots, x_k)$, how can you determine whether Player A or Player B has a guaranteed winning strategy? What is the explicit winning move?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution (Bouton's Theorem)</b></summary>

<br>

### 1. The Nim-Sum ($\oplus$ Bitwise XOR)
In 1901, Charles L. Bouton proved that the state of any Nim game is completely characterized by the **Nim-Sum** of the pile sizes, defined as the bitwise exclusive OR ($\text{XOR}$, denoted as $\oplus$):

$$S = x_1 \oplus x_2 \oplus \dots \oplus x_k$$

To compute $S$:
1. Write each pile size in binary.
2. Sum the bits in each column without carrying over (modulo 2 sum per column).

---

### 2. Winning and Losing Positions

- **Losing Position ($P$-position / Previous player wins):**
  $$S = x_1 \oplus x_2 \oplus \dots \oplus x_k = 0$$
  If the board has a Nim-sum of $0$, any valid move **strictly changes** the Nim-sum to a non-zero value ($S \neq 0$).

- **Winning Position ($N$-position / Next player wins):**
  $$S = x_1 \oplus x_2 \oplus \dots \oplus x_k \neq 0$$
  If the board has a Nim-sum $S \neq 0$, there **always exists at least one valid move** that restores the Nim-sum to $0$.

---

### 3. How to Construct the Winning Move
If $S \neq 0$:
1. Find the **Most Significant Bit (MSB)** of $S$ (the leftmost $1$ in binary).
2. Pick any pile $x_i$ that has a $1$ in that same bit position. (Such a pile is guaranteed to exist).
3. Change the size of that pile from $x_i$ to $x_i' = x_i \oplus S$.
4. Since $x_i \oplus S < x_i$, this move strictly reduces the pile (it is always legal).
5. The new Nim-sum after the move becomes:
   $$S' = S \oplus x_i \oplus x_i' = S \oplus x_i \oplus (x_i \oplus S) = 0$$

By repeatedly handing the opponent a position with $S = 0$, the winning player will inevitably make the final move down to the terminal state $(0, 0, \dots, 0)$, where $S = 0$.

---

### 4. Worked Example: 3 Piles of $(3, 4, 5)$

Write the numbers in binary:
```text
Pile 1:  3 = 0 1 1_2
Pile 2:  4 = 1 0 0_2
Pile 3:  5 = 1 0 1_2
--------------------
Nim-Sum: S = 0 1 0_2 = 2  (Non-zero -> Player A can win!)
