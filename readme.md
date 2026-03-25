## 🎯 Lasso Regression (L1 Regularization)

**Lasso** stands for *Least Absolute Shrinkage and Selection Operator*. Think of it as standard Linear Regression but with a "penalty" (a fine) attached to it.

### 💡 The Core Concept
In a standard model, the algorithm only cares about minimizing the error. Lasso adds a constraint: 
> "Minimize the error, **BUT** the larger your coefficients ($\beta$) are, the higher the penalty you receive."

### 🚀 The "Magic" of L1 Penalty
Lasso uses what is called an **L1 Penalty** (Absolute Value). Mathematically, this specific shape has a unique property: it can force certain coefficients to become **exactly zero**.

<<<<<<< HEAD
###  Key Outcomes

* **✨ Automatic Feature Selection**
    This is Lasso’s "superpower." By using an **L1 penalty**, the algorithm can shrink the coefficients of less important variables to **exactly zero**. If your dataset has 100 variables but only 10 actually drive the result, Lasso will automatically ignore the 90 "noise" variables.

* **📖 Model Simplicity & Sparsity**
    Because it forces irrelevant weights to zero, it creates a **sparse model**. This makes the final equation much shorter and easier for humans to interpret compared to a standard regression where every variable has a tiny, confusing weight.

* **🛡️ Fighting Overfitting**
    Standard regression often "over-memorizes" the training data (including the noise). Lasso prevents this by penalizing large coefficients. 
    > **Note:** Adding a **$\lambda$ (Lambda) penalty** reduces model complexity, which effectively minimizes **overfitting** and allows the model to generalize better to new, unseen data.

---

### 📉 The Impact of $\lambda$ (Regularization)

| Lambda ($\lambda$) | Effect on Model | Result |
| :--- | :--- | :--- |
| **$\lambda = 0$** | No Penalty | Standard Linear Regression (High Overfit Risk) |
| **Low $\lambda$** | Light Shrinkage | Most features kept, weights slightly reduced |
| **High $\lambda$** | Aggressive Shrinkage | **Feature Selection** occurs (Many weights become 0) |

---

### 🧮 The Cost Function
$$Cost = \text{RSS} + \lambda \sum_{j=1}^{p} |\beta_j|$$

* **RSS:** Residual Sum of Squares (The error).
* **$\lambda$ (Lambda):** The tuning parameter. 
    * If $\lambda = 0$: It behaves like a standard Linear Regression.
    * As $\lambda$ increases: More coefficients are pushed to zero, making the model simpler.
