## Day 6 — Scikit-learn Fundamentals

**Goal:** Understand the core ML workflow in scikit-learn — preprocessing, pipelines, and the fit/predict pattern.

---

### Block 1 — Encode and Scale (30 min)

Your IBM dataset has both categorical and numeric columns. Before any model can touch it:

- Encode categorical columns like `OverTime`, `Department`, `Gender` using `LabelEncoder` or `get_dummies`
- Scale numeric columns like `MonthlyIncome`, `Age`, `YearsAtCompany` using `StandardScaler`
- Also encode your target column `Attrition` — convert `Yes/No` to `1/0`

Write a markdown cell explaining why scaling matters for some models but not others.

---

### Block 2 — Train/Test Split (20 min)

- Split your data into 80% train and 20% test using `train_test_split`
- Use `random_state=42` for reproducibility
- Check the shape of all 4 variables — `X_train`, `X_test`, `y_train`, `y_test`
- Check class balance in both splits — is attrition ratio similar in train and test?

---

### Block 3 — Build a Sklearn Pipeline (40 min)

This is the most important block of the day. A pipeline chains preprocessing + model into one clean object:

- Build a `Pipeline` with two steps: a scaler and a placeholder `LogisticRegression` model
- Fit it on training data only — never on test data
- Predict on test data

Write a markdown cell explaining what data leakage is and how the pipeline prevents it.

---

### Block 4 — Intentional Leakage Exercise (20 min)

This is the most valuable exercise of the day — deliberately break your pipeline:

- Fit the scaler on the entire dataset before splitting
- Train and evaluate the model
- Compare results to your clean pipeline
- Write what you observe in markdown

Understanding leakage by seeing it is better than reading about it 10 times.

---

### Block 5 — First Evaluation (20 min)

- Print a `classification_report` on your test predictions
- Don't just look at accuracy — focus on precision, recall, and F1 for the `Yes` class (churned)
- Write why accuracy is misleading here given the class imbalance you found on Day 5

---

### GitHub Push
Commit as `day06_sklearn_intro.ipynb`

---

## End of Day Checklist
- [ ] Categorical and numeric columns preprocessed correctly
- [ ] Pipeline built and fitted on training data only
- [ ] Leakage exercise done and documented in markdown
- [ ] Classification report interpreted in markdown
- [ ] Pushed to GitHub
