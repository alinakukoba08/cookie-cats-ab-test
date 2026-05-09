# 🎮 Cookie Cats A/B Test Analysis

This project analyzes an A/B test conducted on the mobile game *Cookie Cats*, where the position of a gameplay “gate” was changed from level 30 (`gate_30`) to level 40 (`gate_40`). The goal is to evaluate how this change affects player retention.

---

## 📌 Objective

The main objective is to determine whether moving the first in-game gate impacts:

- 📅 Day 1 retention (short-term engagement)
- 📅 Day 7 retention (long-term engagement)

---

## 📂 Dataset

The dataset contains user-level behavior data for two experimental groups:

- `gate_30` — original version with gate at level 30  
- `gate_40` — modified version with gate at level 40  

### Key variables:
- `version` — experiment group
- `retention_1` — user returned after 1 day (True/False)
- `retention_7` — user returned after 7 days (True/False)

---

## 🛠 Tools & Libraries

- Python 🐍
- Pandas
- SciPy (chi-square test)
- Math (confidence intervals)

---

## 🔍 Methodology

The analysis includes:

1. Group-wise retention comparison
2. Statistical significance testing (Chi-square test)
3. Confidence interval estimation for retention rates

---

## 📊 Results

### 📅 Retention Rates

| Version   | Day 1 Retention | Day 7 Retention |
|-----------|----------------|----------------|
| gate_30   | 44.8%          | 19.0%          |
| gate_40   | 44.2%          | 18.2%          |

---

### 📈 Statistical Significance

#### Day 1 Retention
- p-value: **0.0755**
- Result: ❌ Not statistically significant

#### Day 7 Retention
- p-value: **0.0016**
- Result: ✅ Statistically significant

---

### 📏 Confidence Intervals (Day 7 Retention)

- **gate_30:** (18.66%, 19.38%)  
- **gate_40:** (17.85%, 18.55%)

---

## 📌 Key Insights

- No significant difference in short-term retention (Day 1)
- Significant decrease in long-term retention (Day 7) for `gate_40`
- Players in `gate_30` version show better engagement over time

---

## ✅ Conclusion

Moving the gate from level 30 to level 40 did **not improve retention**. In fact, it **negatively impacted long-term user engagement**.  

Based on the results, the recommended decision is to **keep the gate at level 30**.

---

## 📓 Notebook

You can view the full analysis in the Jupyter Notebook:

👉 `cookie_cats_ab_test.ipynb`

---

## 🚀 Future Improvements

- Add visualization of retention trends
- Perform additional A/B tests (e.g., revenue impact)
- Apply Bayesian A/B testing for deeper analysis

---

## 📬 Author

Created as part of a data analysis and A/B testing portfolio project.
