# 🟠 Two Frogs on a Grid (Manhattan Distance Expected Meeting Time)

## 🎯 Problem Statement
Two frogs start at two different positions on an infinite two-dimensional grid ($\mathbb{Z}^2$). 
- At each discrete time step, each frog independently chooses one of the **4 adjacent directions** (North, South, East, West) uniformly at random and jumps to that neighboring cell.
- The **Manhattan distance** between two points $(x_1, y_1)$ and $(x_2, y_2)$ is defined as:
  $$d((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2|$$

### ❓ Question
If the two frogs start at an initial Manhattan distance $d_0$, what is the **expected number of steps** until they land on the exact same cell for the first time?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Martingale / Green's Function Approach</b></summary>

<br>

### 1. Transforming to a Single Random Walk
Instead of tracking the independent positions of Frog 1 $(x_1, y_1)$ and Frog 2 $(x_2, y_2)$, we can simplify the problem by analyzing their **relative position vector** $(X, Y) = (x_1 - x_2, y_1 - y_2)$.

Because both frogs move independently and symmetrically:
- In each time step, the relative coordinates $(X, Y)$ change according to a combined random walk.
- Specifically, with probability $1/2$, the Manhattan distance $d = |X| + |Y|$ either **increases by 1** or **decreases by 1**, while on certain steps it can also change by 0 (depending on whether moves are parallel or perpendicular). More precisely, on any given step, the Manhattan distance changes by $+1$ with probability $1/2$ and by $-1$ with probability $1/2$ in a 1D-like projection along the coordinate axes.

---

### 2. The Recurrence Relation for Expected Time
Let $E(d)$ be the expected number of steps for the frogs to meet, starting from an initial Manhattan distance $d$.

When the frogs are at distance $d > 0$:
- In the next step, the distance becomes $d - 1$ with probability $p$ or $d + 1$ with probability $1-p$.
- Due to the geometry of the 2D grid, the drift is zero (symmetric random walk on distance), leading to the second-order difference equation:
  $$E(d) = 1 + \frac{1}{4} E(d-1) + \frac{1}{4} E(d+1) + \frac{1}{2} E(d)$$ *(accounting for diagonal/axis transition weights on $\mathbb{Z}^2$)*

Solving this system requires handling the boundary condition at $d = 0$ (where $E(0) = 0$, since they have met).

---

### 3. The Asymptotic Behavior in 2D
Unlike 1D grids where expected meeting times for finite domains scale quadratically ($O(N^2)$), **infinite 2D grids are recurrent, but logarithmic/linear escape properties change things**. 

For two independent random walkers on $\mathbb{Z}^2$:
- The expected time to hit the exact same node starting from distance $d_0$ diverges to infinity. 
- Formally, the Green's function for the simple random walk on $\mathbb{Z}^2$ grows logarithmically with distance, meaning that **the expected hitting time is infinite ($E = \infty$)** for starting points on an infinite 2D grid. 
- *Intuition:* Even though they are guaranteed to meet eventually (due to 2D recurrence), paths can wander arbitrarily far away before intersecting, causing the tail of the distribution to be too heavy for a finite expected value.

</details>
