# 🟢 Trailing Zeros of 1000! (Factorial)

## 🎯 Problem Statement
Consider the factorial of one thousand, denoted as **$1000!$** (the product of all integers from 1 to 1000):
$$1000! = 1 \times 2 \times 3 \times \dots \times 999 \times 1000$$

### ❓ Question
How many consecutive **trailing zeros** does the decimal representation of $1000!$ end with?

---

<details>
<summary><b>💡 Click to Reveal the Analytical Solution & Prime Factorization Proof</b></summary>

<br>

### 1. The Prime Factorization Insight
A trailing zero in any integer is created by multiplying by $10$. Prime-factorizing $10$ gives:
$$10 = 2 \times 5$$

Therefore, each trailing zero corresponds to a pair of prime factors **$(2, 5)$** in the prime factorization of $1000!$.

* In any factorial $N!$, the number of prime factor $2$s vastly outnumbers the number of prime factor $5$s.
* Thus, the number of trailing zeros is strictly determined by **the total multiplicity of the prime factor $5$** in $1000!$.

---

### 2. Legendre's Formula
To find the exponent of a prime $p$ dividing $n!$, we use **Legendre's Formula**:
$$E_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor$$

For $p = 5$ and $n = 1000$, this expands to counting:
1. Multiples of $5$ between 1 and 1000.
2. Multiples of $5^2 = 25$ (which contribute an extra factor of 5).
3. Multiples of $5^3 = 125$ (contributing a third factor of 5).
4. Multiples of $5^4 = 625$ (contributing a fourth factor of 5).
5. Higher powers ($5^5 = 3125 > 1000$, so the sum stops).

---

### 3. Step-by-Step Calculation
$$\left\lfloor \frac{1000}{5} \right\rfloor = 200$$

$$\left\lfloor \frac{1000}{25} \right\rfloor = 40$$

$$\left\lfloor \frac{1000}{125} \right\rfloor = 8$$

$$\left\lfloor \frac{1000}{625} \right\rfloor = 1$$

Summing these terms together:
$$\text{Total Zeros} = 200 + 40 + 8 + 1 = \mathbf{249}$$

Thus, $1000!$ ends with **249 consecutive trailing zeros**.

</details>
