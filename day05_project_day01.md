# Day 5 — Mini Project Day 1: Problem Framing + EDA

**Goal:** Start your end-to-end mini project. Today is about picking your dataset, defining the problem, and doing a full EDA.

---

## Dataset
Use the **IBM HR Analytics Attrition Dataset** — download from Kaggle:
🔗 [IBM HR Analytics Dataset](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## Block 1 — Define the Problem (20 min)
Before touching the data, write a markdown cell answering:
- What is the business problem in 1-2 sentences?
- What are you predicting?
- Why does it matter to the business?

---

## Block 2 — First Look at the Data (20 min)
- Shape, dtypes, null check, duplicates
- How many employees churned vs stayed? (class balance check)
- Write your observations in markdown

---

## Block 3 — Full EDA (60 min)
- Distribution of `Age`, `MonthlyIncome`, `YearsAtCompany`
- Attrition rate by `Department`, `JobRole`, `OverTime`
- Correlation heatmap — which numeric features correlate with `Attrition`?

Write one insight per chart.

---

## Block 4 — Identify Key Features (30 min)
Pick 5 features you think will matter most for predicting attrition and explain why in markdown — use business logic, not just correlation numbers.

---

## GitHub Push
Create a `mini-project/` folder, commit as `mini-project/01_eda.ipynb`

---

## End of Day Checklist
- [x] Business problem written clearly in markdown
- [x] Class imbalance identified and noted
- [x] At least 6 charts with interpretations
- [x] 5 features selected with reasoning
- [x] Pushed to GitHub under `mini-project/`