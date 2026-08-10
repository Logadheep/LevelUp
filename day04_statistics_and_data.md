# Day 4 — Statistics That Actually Matter

**Goal:** Apply just enough statistics to support your DS work — no textbook theory, only things you'll actually use.

---

## Block 1 — Central Tendency & Spread (20 min)
- Calculate mean, median, std, and IQR for `Age` and `Fare`
- Where mean and median differ a lot — what does that tell you?
- Write your interpretation in a markdown cell

---

## Block 2 — Distributions (30 min)
Watch these two StatQuest videos:
- *"Normal Distribution, Clearly Explained"*
- *"Standard Deviation, Clearly Explained"*

Then check: is `Age` normally distributed? Is `Fare`? Use a plot to support your answer.

---

## Block 3 — Hypothesis Testing (40 min)
Answer statistically: **"Did women have a significantly higher survival rate than men?"**
- Use `scipy.stats.ttest_ind` to compare the two groups
- Print the p-value
- Explain the result in plain English in markdown — as if telling a non-technical manager

Then ask a second question of your own and test it the same way.

---

## Block 4 — Chi-Square Test (30 min)
Answer: **"Is there a relationship between passenger class and survival?"**
- Use `scipy.stats.chi2_contingency`
- Build a crosstab first, then run the test
- Interpret the result in markdown

---

## Block 5 — Wrap It Up (20 min)
Write a final markdown cell summarising:
- 3 statistical findings from today
- What each finding would mean if you were advising the shipping company

---

## GitHub Push
Commit as `day04_statistics.ipynb`

---

## End of Day Checklist
- [x] At least 2 hypothesis tests run and interpreted
- [x] Every result explained in plain English in markdown
- [x] No copy-pasted interpretations — write them yourself
- [x] Pushed to GitHub