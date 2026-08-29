# 🟢 The Subtraction Game (1-Pile Nim)

## 🎯 Problem Statement
Two players, **Player A** and **Player B**, play a turn-based game with a single pile of **$21$ matchsticks** (or stones).

- Player A moves first.
- On their turn, a player may remove **$1$, $2$, or $3$** matchsticks from the pile.
- **Normal Play Rule:** The player who takes the **very last matchstick** wins the game.

Assuming both players play with optimal strategy, which player is guaranteed to win, and what is the winning strategy?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Proof</b></summary>

<br>

### 1. Invariant & Modular Arithmetic
The key to subtraction games is finding the **complementary step size**.

Because a player can choose $k \in \{1, 2, 3\}$, whatever number of items Player A chooses, Player B can always choose $4 - k$ to reduce the pile by exactly **$4$ items per round**:
- If A takes $1$, B takes $3$ ($1 + 3 = 4$).
- If A takes $2$, B takes $2$ ($2 + 2 = 4$).
- If A takes $3$, B takes $1$ ($3 + 1 = 4$).

---

### 2. Identifying Winning and Losing Positions
Let $N$ be the number of matchsticks remaining:

- **Losing Positions ($P$-positions):** Any multiple of $4$ ($N \equiv 0 \pmod 4$).  
  Whichever number ($1, 2, 3$) the current player removes, the next player can always restore the pile to a multiple of $4$.
- **Winning Positions ($N$-positions):** Any number not divisible by $4$ ($N \not\equiv 0 \pmod 4$).  
  The current player can remove $(N \pmod 4)$ matchsticks to leave the opponent in a losing state ($0 \pmod 4$).

---

### 3. Step-by-Step Game Progression ($N = 21$)

Since the game starts at $21$:
$$21 \pmod 4 = 1$$

1. **Move 1:** Player A takes **$1$ matchstick**, leaving $20$ (a multiple of $4$).
2. **Move 2:** If Player B takes $k$ matchsticks, Player A responds by taking $4 - k$ matchsticks, leaving $16$.
3. **Subsequent Moves:** Player A continuously mirrors Player B to leave $12 \to 8 \to 4 \to 0$ matchsticks.
4. **Final Step:** When Player B faces $4$ matchsticks and takes $k \in \{1, 2, 3\}$, Player A takes the remaining $4 - k$ matchsticks, claiming the last matchstick and winning the game.

**Conclusion:** **Player A (First Player)** has a guaranteed winning strategy by taking $1$ matchstick on the opening turn.

</details>
