# 🟠 Expected Intersections of 10 Random Chords in a Circle

## 🎯 Problem Statement
Suppose you choose **$20$ distinct points** uniformly and independently at random on the circumference of a circle, and pair them up randomly to form **$10$ chords**.

### ❓ Question
What is the **expected (average) number of intersection points** formed by these 10 chords inside the circle?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Linearity of Expectation</b></summary>

<br>

### 1. The Core Geometric Insight
Any single chord is defined by 2 endpoints on the circle. Therefore, $10$ chords are formed by choosing $20$ points uniformly and pairing them at random.

Two random chords inside a circle intersect **if and only if** their 4 endpoints alternate along the circumference (e.g., in clockwise order: Point 1, Point 2, Point 1, Point 2).

---

### 2. Probability That Two Chords Intersect
If we pick any **4 random points** on a circle, there are $\binom{4}{2} = 6$ possible ways to pair them into 2 chords:
* Exactly **2 pairings** result in the chords crossing each other inside the circle.
* The remaining **4 pairings** do not intersect.

Thus, the probability that any two arbitrarily chosen chords intersect is:
$$P(\text{Intersection}) = \frac{2}{6} = \frac{1}{3}$$

---

### 3. Applying Linearity of Expectation
With $N = 10$ chords, the total number of distinct pairs of chords that can potentially intersect is given by the binomial coefficient:
$$\text{Total Chord Pairs} = \binom{10}{2} = \frac{10 \times 9}{2} = 45$$

By the **Linearity of Expectation**, the expected total number of intersections $E[I]$ is the sum of the probabilities over all possible pairs:
$$E[I] = \binom{N}{2} \cdot P(\text{Intersection}) = \binom{10}{2} \cdot \frac{1}{3}$$

$$E[I] = 45 \cdot \frac{1}{3} = \mathbf{15}$$

The expected number of intersections for 10 random chords is exactly **15**.

</details>
