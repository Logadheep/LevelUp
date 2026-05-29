# Day 3 — Exploratory Data Analysis (EDA)

**Goal:** Take your cleaned Day 2 dataset and tell a visual story with it.

---

## Setup
Load your cleaned dataframe from Day 2 — import your `clean_titanic()` function or re-run Day 2's notebook.

---

## Block 1 — Distributions (30 min)
- Plot histograms for `Age` and `Fare`
- Plot countplots for `Survived`, `Pclass`, and `Sex`
- Write one insight per plot in markdown — interpret, don't just describe

---

## Block 2 — Boxplots for Outlier Detection (20 min)
- Plot boxplots for `Age` and `Fare`
- Identify if outliers are real data or errors
- Write your conclusion in markdown

---

## Block 3 — Correlation Heatmap (20 min)
- Generate a heatmap of numeric column correlations
- Identify which features correlate most with `Survived`
- Write your top 3 findings in markdown

---

## Block 4 — Survival Deep Dives (40 min)
Answer these visually — one chart per question:
- Did gender affect survival?
- Did passenger class affect survival?
- Did family size affect survival?
- Did age distribution differ between survivors and non-survivors?

Write 2 sentences per chart — what you see and what it means.

---

## Block 5 — Find 3 Non-Obvious Insights (30 min)
Dig into combinations:
- Did being alone vs with family matter differently across classes?
- Was there an age sweet spot for survival?
- Did fare paid correlate with survival even within the same class?

Write each insight in plain English like you're explaining to a non-technical manager.

---

## GitHub Push
Commit as `day03_eda.ipynb` — this is your first real portfolio piece. Make it clean.

---

## End of Day Checklist
- [x] At least 8 charts total
- [x] Every chart has a markdown interpretation below it
- [x] 3 non-obvious insights written in plain English
- [x] Notebook runs top to bottom without errors
- [x] Pushed to GitHub