## Day 8 — Classification Models

**Goal:** Train and compare 3 classification models on your IBM attrition dataset — and this time, you'll actually understand the math behind at least one of them.

---

### Block 1 — Train Three Models (60 min)

Using the pipeline setup from Day 6, train three different classifiers on your preprocessed data:

- **Logistic Regression** — you now know exactly what this is doing under the hood
- **Decision Tree**
- **Random Forest**

Keep default hyperparameters for now — this is about comparing model *families*, not tuning yet.

---

### Block 2 — Compare Performance (40 min)

For each model:
- Print a `classification_report` on the test set
- Focus on **precision, recall, and F1 for the "Yes" class** (attrition), not overall accuracy — you already know why from Day 4/6

Write a markdown cell comparing the three models: which one has the best recall for the minority class? Which has the best precision? Is there a tradeoff?

---

### Block 3 — Why Accuracy Lies Here (20 min)

Calculate what accuracy a model would get if it **always predicted "No"** (never predicted attrition at all). Compare that number to your actual models' accuracy.

Write a markdown cell explaining why this number is dangerously high, and why precision/recall/F1 matter more for this problem.

---

### Block 4 — Model Intuition (30 min)

Without needing full derivations like you did for Logistic Regression, write a short markdown note for Decision Tree and Random Forest answering:
- How does a Decision Tree actually make a decision at each split?
- Why does Random Forest tend to outperform a single Decision Tree?

This is conceptual, not mathematical — just enough to explain *why* the models behave differently in your comparison above.

---

### GitHub Push
Commit as `mini-project/02_models.ipynb`

---

## End of Day Checklist
- [ ] All 3 models trained and evaluated on the same test set
- [ ] Classification reports interpreted, not just printed
- [ ] "Always predict No" baseline calculated for contrast
- [ ] Model comparison written in plain English
- [ ] Pushed to GitHub
