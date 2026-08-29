# 🎲 Mastering Probability & Quantitative Brainteasers

A curated collection of classical and modern probability puzzles, combinatorics problems, and stochastic brainteasers frequently asked in **Quantitative Trading & Research interviews** (Optiver, Jane Street, Citadel, SIG, IMC).

Each problem includes an analytical step-by-step mathematical proof, intuition breakdown, and (where applicable) a Monte Carlo simulation script in Python.

---

## 🚦 Difficulty Legend

Problems are classified across 4 tiers of analytical and mathematical complexity:

| Tier | Badge | Description |
| :--- | :---: | :--- |
| **Easy** | 🟢 | Warm-up problems, standard symmetry, direct formulas, or basic conditional probability. |
| **Medium** | 🟠 | Multi-step reasoning, Markov chains, recurrences, or non-trivial combinatorial counting. |
| **Difficult** | 🔴 | Advanced continuous distributions, coupling arguments, generating functions, or subtle invariants. |
| **Impossible** | 💀 | Legendary brainteasers, counter-intuitive paradoxes, or multi-layered optimization problems. |

---

## 📚 Problem Catalog

| # | Difficulty | Problem Name | Core Concepts / Tags | Folder |
| :-: | :-: | :--- | :--- | :--- |
| `01` | 🟢 | **Fair Probability from an Unfair Coin** | Symmetry, Von Neumann Extractor, Bernoulli Trials | [`01_von_neumann`](./01_von_neumann/) |
| `02` | 🟢 | **Hopping Rabbit** | Recurrence Relations, Fibonacci Sequence | [`02_hopping_rabbit`](./02_hopping_rabbit/) |
| `03` | 🟢 | **Trailing Zeros in Factorials** | Legendre's Formula, Prime Factorization | [`03_trailing_zeros`](./03_trailing_zeros/) |
| `04` | 🟠 | **Drunk Passenger** | Invariance, Symmetry Principle, Martingales | [`04_drunk_passenger`](./04_drunk_passenger/) |
| `05` | 🟠 | **N Points on a Circle** | Geometric Probability, Arc Coverage, Disjoint Events | [`05_n_points_circle`](./05_n_points_circle/) |
| `06` | 🟠 | **25 Horses Race** | Min-Max Tournament Sort, Decision Trees | [`06_25_horses`](./06_25_horses/) |
| `07` | 🔴 | **12 Defective Balls & Balance Scale** | Information Theory, Ternary Search, Partitioning | [`07_defective_balls`](./07_defective_balls/) |
| `08` | 🔴 | **Marble Swap Chain** | Markov Chains, Transition Matrices, Stationary Dist. | [`08_marble_swap`](./08_marble_swap/) |
| `09` | 💀 | **Frog with One Left Jump** | Permutation Descents, Eulerian Numbers, Order Stats | [`09_frog_one_left_jump`](./09_frog_one_left_jump/) |

---

## 📖 Primary References & Literature

This collection draws inspiration from foundational quantitative finance literature, recreational mathematics, and competitive problem solving:

1. **A Practical Guide to Quantitative Finance Interviews** — *Xinfeng Zhou*
2. **Fifty Challenging Problems in Probability with Solutions** — *Frederick Mosteller*
3. **Heard on the Street: Quantitative Questions from Wall Street Job Interviews** — *Timothy Falcon Crack*
4. **Quant Job Interview Questions and Answers** — *Mark Joshi, Nicholas Denson, Andrew Downes*
5. **Problems in Applied Mathematics / Probability and Random Processes** — *Geoffrey Grimmett & David Stirzaker*
6. **The Colossal Book of Mathematics** — *Martin Gardner*

---

## 🛠️ Repository Structure & Usage

Each subfolder contains:
- `README.md`: Formal mathematical derivation, intuition notes, and LaTeX formulations.
- `solution.py` *(optional)*: Monte Carlo verification script to empirically validate theoretical probabilities.

### Run a simulation locally
```bash
python3 01_von_neumann/solution.py
