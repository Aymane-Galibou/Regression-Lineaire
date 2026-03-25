## 🎯 Lasso Regression (L1 Regularization)

**Lasso** stands for *Least Absolute Shrinkage and Selection Operator*. Think of it as standard Linear Regression but with a "penalty" (a fine) attached to it.

### 💡 The Core Concept
In a standard model, the algorithm only cares about minimizing the error. Lasso adds a constraint: 
> "Minimize the error, **BUT** the larger your coefficients ($\beta$) are, the higher the penalty you receive."

### 🚀 The "Magic" of L1 Penalty
Lasso uses what is called an **L1 Penalty** (Absolute Value). Mathematically, this specific shape has a unique property: it can force certain coefficients to become **exactly zero**.

### 📊 Key Outcomes:
* **Feature Selection:** This is Lasso’s superpower. If you have 100 input variables and 90 of them are useless noise, Lasso will ignore them entirely by setting their weights to zero.
* **Simplicity:** It produces a "sparse" model that is much easier to interpret than a standard regression.
* **Prevents Overfitting:** By penalizing large coefficients, it ensures the model doesn't "over-memorize" the training data ,(adding a $$\lambda penalty to the model reduce the overfitting).

---

### 🧮 The Cost Function
$$Cost = \text{RSS} + \lambda \sum_{j=1}^{p} |\beta_j|$$

* **RSS:** Residual Sum of Squares (The error).
* **$\lambda$ (Lambda):** The tuning parameter. 
    * If $\lambda = 0$: It behaves like a standard Linear Regression.
    * As $\lambda$ increases: More coefficients are pushed to zero, making the model simpler.