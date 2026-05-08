# Cookie Cats A/B Test — Retention Analysis

## About this project

This project analyzes an A/B test from the mobile game Cookie Cats.

The goal is to evaluate whether moving a progression gate affects player retention.

Dataset: Kaggle Cookie Cats A/B test dataset.

---

## Business problem

Players were dropping off early in the game.

We tested whether moving the gate from level 30 to level 40 improves retention.

---

## Groups

- Control: gate at level 30  
- Variant: gate at level 40  

---

## Metrics

- Day 1 retention  
- Day 7 retention  
- Game rounds (engagement)

---

## Approach

- SQL data aggregation
- Python statistical analysis
- Chi-square test
- Confidence intervals

---

## Conclusion

No strong improvement in short-term retention.  
Slight positive signal for long-term retention, but not statistically strong.

Recommendation: do not roll out without further testing.
