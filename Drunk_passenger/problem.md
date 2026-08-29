# 🟠 The Drunk Passenger Problem

## 🎯 Problem Statement
An airplane has **100 seats**, and there are **100 passengers** boarding the plane in order from passenger 1 to passenger 100. Each passenger has a ticket assigned to a specific seat.

- **Passenger 1** is completely drunk. When he boards, he ignores his assigned seat, picks a seat **uniformly at random** among all 100 seats, and sits down.
- Every subsequent passenger ($2$ through $100$) boards the plane:
  - If their assigned seat is **empty**, they sit in it.
  - If their assigned seat is **already occupied**, they choose an empty seat **uniformly at random** among all remaining available seats.

### ❓ Question
What is the exact probability that the **last passenger (Passenger 100)** finds their assigned seat unoccupied when they board?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Proof</b></summary>

<br>

### 1. Defining the Core Symmetry
Let $P(n)$ be the probability that the last passenger gets their correct seat in an airplane with $n$ seats. 

Instead of jumping into complex combinatorial cases for every intermediate passenger, consider the fate of only two specific seats as the boarding process unfolds:
1. **Seat 1** (belonging to the drunk Passenger 1).
2. **Seat 100** (belonging to the last Passenger 100).

As passengers board one by one, seats are gradually filled. Notice what happens to the remaining empty seats:
* If at any point someone is forced to choose a random seat, they could pick Seat 1, Seat 100, or any other seat.
* However, the game effectively ends the exact moment either **Seat 1** or **Seat 100** is chosen by *anyone*.

---

### 2. The Inductive / Recursive Insight
Let's analyze the choice faced by the very first person who has to pick randomly (which starts with Passenger 1, but could happen to someone else if their seat was already taken):

* If Passenger 1 chooses **Seat 100**, then Passenger 100 arrives later and finds their seat occupied. **Probability of success = 0**.
* If Passenger 1 chooses **Seat 1**, then Passenger 1 sits down, and every subsequent passenger ($2$ through $99$) finds their correct seat unoccupied. Therefore, Passenger 100 walks in and finds Seat 100 empty. **Probability of success = 1**.
* If Passenger 1 chooses some intermediate seat $k$ (where $1 < k < 100$):
  - Passenger 1 takes seat $k$.
  - Passengers $2$ through $k-1$ find their correct seats.
  - When Passenger $k$ boards, their seat is taken. Passenger $k$ now acts as a "new drunk passenger" choosing randomly among the remaining seats $\{1, k+1, k+2, \dots, 100\}$.

This reduces the problem of size $100$ to an identical problem of size $101 - k$.

---

### 3. Solving the General Probability $P(N)$
By symmetry and induction, for a plane with $N$ seats, the probability that the last passenger gets their seat is always:

$$P(N) = \frac{1}{2}$$

Regardless of whether there are 100, 1,000, or a million passengers, the probability that the last passenger gets their assigned seat is **precisely 50% ($0.5$)**.

</details>
