# 🎲 Mastering Probability & Quantitative Brainteasers

A curated collection of classical and modern probability puzzles, combinatorics problems, and stochastic brainteasers frequently asked in quantitative interviews and maths olympiads.

Each problem includes:
- A rephrased problem statement and intuitive breakdown.
- A rigorous, step-by-step mathematical proof.
- *(Where applicable)* A Python script featuring Monte Carlo simulations and statistical validation.

---

## 🚦 Difficulty Legend

Problems are categorized into 4 tiers of mathematical and analytical complexity:

| Tier | Badge | Description |
| :--- | :---: | :--- |
| **Easy** | 🟢 | Warm-up problems, basic symmetry, direct formulas, or simple conditional probability. |
| **Medium** | 🟠 | Markov chains, recurrences, or non-trivial combinatorial counting. |
| **Difficult** | 🔴 | Advanced continuous distributions, generating functions, or subtle invariants. |
| **Impossible** | 💀 | good luck. |

---
## ⚙️ A Note on Randomness & Simulations (PRNG)

All empirical verifications in this repository rely on Python's standard `random` module or NumPy. It is worth noting:

* **Pseudo-Randomness (PRNG):** Python's `random` uses the **Mersenne Twister** algorithm (with a period of $2^{19937}-1$). It is a deterministic mathematical formula that generates a sequence of numbers that *mimics* true randomness starting from an initial seed.
* **Empirical Validation vs Proof:** Monte Carlo simulations serve as numerical approximations to verify expected values and distributions. They confirm that our theoretical formulas match empirical observations, but are not a substitute for formal mathematical proofs.

## 📖 Primary References & Literature

This collection draws inspiration from classic quantitative finance literature, recreational mathematics, and competitive problem solving:

1. **A Practical Guide to Quantitative Finance Interviews** — *Xinfeng Zhou*
2. **Fifty Challenging Problems in Probability with Solutions** — *Frederick Mosteller*
3. **Heard on the Street: Quantitative Questions from Wall Street Job Interviews** — *Timothy Falcon Crack*
4. **Quant Job Interview Questions and Answers** — *Mark Joshi, Nicholas Denson, Andrew Downes*
5. **Probability and Random Processes** — *Geoffrey Grimmett & David Stirzaker*
6. **The Colossal Book of Mathematics** — *Martin Gardner*

---

## 🛠️ Repository Structure & Usage

Each subfolder corresponds to a specific problem:
- `README.md`: Formal analytical derivations, intuition notes, and LaTeX formulations.
- `solution.py` / `simulation.py`: Numerical checks and Monte Carlo empirical validations.

### Running a simulation locally
```bash
python3 <folder_name>/solution.py
