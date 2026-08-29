# 🟢 Measuring 45 Minutes with Two Burning Ropes

## 🎯 Problem Statement
You are given **two ropes** (or fuses) and a box of matches.

- Each rope takes **exactly 60 minutes** to burn completely from one end to the other.
- The ropes are **heterogeneous / non-uniform**: the rate of burning is uneven along their length (e.g., half the rope might take 50 minutes to burn, and the remaining half only 10 minutes).
- The two ropes are not necessarily identical in their burn rate distribution.
- You have no other measuring devices (no clock, no ruler to cut them).

### ❓ Question
How can you measure an exact interval of **45 minutes** using only these two ropes and matches?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Procedure</b></summary>

<br>

### 1. The Core Insight: Two-End Ignition
Even though a rope burns non-uniformly, lighting **both ends simultaneously** causes the two flames to travel towards each other and meet. 

Regardless of where they meet, the total material that would have taken $60$ minutes to burn with one flame is consumed simultaneously from both sides:
$$\text{Time to fully burn from both ends} = \frac{60 \text{ minutes}}{2} = 30 \text{ minutes}$$

---

### 2. Step-by-Step Procedure

1. **$T = 0$ min (Start the timer):**
   - Take **Rope A** and light **both ends** simultaneously.
   - Take **Rope B** and light **one end only**.

2. **$T = 30$ min (Rope A burns out completely):**
   - Exactly $30$ minutes have elapsed because Rope A is completely consumed.
   - Rope B has been burning for $30$ minutes from one end. Therefore, the unburnt portion of Rope B has exactly **$30$ minutes of burn time remaining** (at single-end speed).
   - At this precise moment, **light the second end of Rope B**.

3. **$T = 45$ min (Rope B burns out completely):**
   - With both ends lit, the remaining $30$ minutes worth of Rope B is consumed in:
     $$\frac{30 \text{ minutes}}{2} = 15 \text{ minutes}$$
   - When Rope B burns out completely, exactly $30 + 15 = \mathbf{45 \text{ minutes}}$ have elapsed from $T = 0$.

</details>
