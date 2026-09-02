# LevelUp: Data Science Learning Repository

A comprehensive learning journey through data science, from pandas basics to machine learning with scikit-learn. This repository contains hands-on Jupyter notebooks, real-world datasets, and utility tools for data exploration and analysis.

---

## 📚 Overview

**LevelUp** is a structured curriculum designed to progressively build data science skills. Each module builds upon previous knowledge, combining theoretical concepts with practical implementations using real datasets.

### What You'll Learn
- **Data Manipulation**: Pandas operations and data structures
- **Data Cleaning**: Handling missing values and data preparation
- **Exploratory Data Analysis**: Statistical analysis and visualization techniques
- **Statistics**: Hypothesis testing and statistical methods
- **Machine Learning**: Introduction to scikit-learn algorithms

---

## 🗂️ Repository Structure

```
LevelUp/
├── README.md                                    # This file
├── repo_utils.py                               # Repository analysis & utilities
├── data_analysis_kit.py                        # Data exploration toolkit
│
├── Notebooks (Learning Modules)
│   ├── day01_pandas_basics.ipynb               # Pandas fundamentals
│   ├── day02_data_cleaning.ipynb               # Data cleaning techniques
│   ├── day04_statistics.ipynb                  # Statistical analysis
│   ├── day06_scikit_learn_intro.ipynb          # Machine learning intro
│
├── Documentation
│   ├── day03_eda_and_visualization.md          # EDA & visualization guide
│   ├── day04_statistics_and_data.md            # Statistics concepts
│   ├── day05_project_day01.md                  # First project guidelines
│   ├── day06_sklearn_intro.md                  # Scikit-learn overview
│
├── datasets/
│   ├── titanic.csv                            # Titanic passenger dataset
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv  # HR employee attrition data
│
└── mini-project/
    └── 01_eda.ipynb                            # Mini-project notebook
```

---

## 📖 Learning Path

Follow this sequence for the best learning experience:

### **Day 01: Pandas Basics** 📊
- Learn fundamental pandas operations
- Master DataFrames and Series
- Practice data indexing and selection
- **Notebook**: [day01_pandas_basics.ipynb](day01_pandas_basics.ipynb)

### **Day 02: Data Cleaning** 🧹
- Handle missing values effectively
- Clean and transform data
- Prepare data for analysis
- **Notebook**: [day02_data_cleaning.ipynb](day02_data_cleaning.ipynb)

### **Day 03: EDA and Visualization** 📈
- Exploratory Data Analysis techniques
- Create meaningful visualizations
- Understand data distributions
- **Documentation**: [day03_eda_and_visualization.md](day03_eda_and_visualization.md)

### **Day 04: Statistics and Data Analysis** 📉
- Statistical foundations and hypothesis testing
- Correlation and regression analysis
- **Notebook**: [day04_statistics.ipynb](day04_statistics.ipynb)
- **Documentation**: [day04_statistics_and_data.md](day04_statistics_and_data.md)

### **Day 05: Project Day** 🎯
- Apply skills to real-world problems
- End-to-end data analysis project
- **Guidelines**: [day05_project_day01.md](day05_project_day01.md)

### **Day 06: Introduction to Scikit-learn** 🤖
- Machine learning fundamentals
- Classification and regression models
- Model evaluation techniques
- **Notebook**: [day06_scikit_learn_intro.ipynb](day06_scikit_learn_intro.ipynb)
- **Documentation**: [day06_sklearn_intro.md](day06_sklearn_intro.md)

### **Mini-Project** 🚀
- Put it all together in [mini-project/01_eda.ipynb](mini-project/01_eda.ipynb)

---

## 📊 Datasets

### Titanic Dataset
- **File**: `datasets/titanic.csv`
- **Description**: Classic Titanic passenger dataset with survival outcomes
- **Use Case**: Binary classification, missing value handling, feature engineering
- **Rows**: 892 | **Columns**: 12

### HR Employee Attrition Dataset
- **File**: `datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv`
- **Description**: Employee attrition patterns and workplace metrics
- **Use Case**: Predictive analytics, feature importance analysis
- **Rows**: 1470 | **Columns**: 35

---

## 🛠️ Utility Tools

### repo_utils.py
Analysis and navigation utilities for the repository:

```python
from repo_utils import LevelUpRepoAnalyzer, load_titanic_dataset, quick_eda

# Initialize analyzer
analyzer = LevelUpRepoAnalyzer(".")

# Display repository structure
analyzer.print_repo_structure()

# Show learning path
analyzer.list_learning_path()

# Load and explore datasets
titanic = load_titanic_dataset()
quick_eda(titanic, "Titanic Dataset")
```

**Key Features:**
- Automatic notebook and dataset discovery
- Repository structure visualization
- Learning path display
- Quick dataset loading functions
- Fast EDA summaries

### data_analysis_kit.py
Comprehensive data exploration and analysis toolkit:

```python
from data_analysis_kit import DataExplorationKit, demonstrate_analysis

kit = DataExplorationKit()

# Load all datasets
datasets = kit.load_all_datasets()

# Analyze missing data
missing_data = kit.analyze_missing_data(df)

# Detect outliers
outliers, stats = kit.get_outliers(df, 'column_name', method='iqr')

# Find correlations
top_correlations = kit.correlation_analysis(df, top_n=10)

# Analyze distributions
distributions = kit.distribution_analysis(df)

# Run demonstrations
demonstrate_analysis()
```

**Key Features:**
- Missing data pattern analysis
- Column type categorization
- Outlier detection (IQR and Z-score methods)
- Correlation analysis
- Distribution assessment
- Built-in demonstration function

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab
- Required packages: pandas, numpy, scikit-learn, matplotlib, seaborn

### Installation

1. Clone or download this repository:
```bash
git clone <repository-url>
cd LevelUp
```

2. Install required packages:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

3. Start Jupyter:
```bash
jupyter notebook
```

4. Open and run notebooks in the suggested learning sequence.

### Using the Utility Tools

Run the repository analyzer:
```bash
python repo_utils.py
```

Run the data analysis demonstration:
```bash
python data_analysis_kit.py
```

Import tools into your notebooks:
```python
from repo_utils import LevelUpRepoAnalyzer, load_titanic_dataset
from data_analysis_kit import DataExplorationKit
```

---

## 💡 Learning Tips

1. **Follow the sequence**: Each module builds on previous concepts
2. **Practice actively**: Run code, experiment with parameters, modify examples
3. **Use the datasets**: Apply techniques to both Titanic and HR Attrition datasets
4. **Read documentation**: Review markdown guides for conceptual understanding
5. **Complete mini-projects**: Reinforce learning through practical applications
6. **Leverage utilities**: Use repo_utils and data_analysis_kit to speed up exploration

---

## 📝 Topics Covered

### Data Manipulation
- DataFrame creation and indexing
- Grouping and aggregation
- Merge and join operations
- Data reshaping

### Data Cleaning
- Missing value imputation
- Outlier detection and handling
- Data type conversion
- Duplicate removal
- Feature scaling

### Exploratory Data Analysis
- Univariate analysis
- Bivariate analysis
- Distribution visualization
- Correlation matrices
- Statistical summaries

### Statistics
- Descriptive statistics
- Hypothesis testing
- Probability distributions
- Correlation and regression
- A/B testing concepts

### Machine Learning
- Supervised learning basics
- Classification algorithms
- Regression models
- Model evaluation metrics
- Train-test splitting
- Cross-validation

---

## 🎓 Skills Development

By completing this curriculum, you'll develop:
- ✅ Data wrangling and preparation skills
- ✅ Statistical analysis capabilities
- ✅ Data visualization expertise
- ✅ Exploratory data analysis proficiency
- ✅ Machine learning fundamentals
- ✅ Problem-solving with real datasets
- ✅ Python programming for data science

---

## 📚 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [NumPy Guide](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples.html)

---

## 📞 Questions & Support

If you encounter issues or have questions:
1. Review the relevant notebook and documentation
2. Check the utility tools for quick diagnostics
3. Run demonstrations to understand data patterns
4. Revisit previous modules if concepts are unclear

---

## 📄 License

This repository is created for educational purposes.

---

## 🎯 Next Steps

1. **Start with Day 01**: Open [day01_pandas_basics.ipynb](day01_pandas_basics.ipynb)
2. **Run the analyzer**: Execute `python repo_utils.py` to explore the structure
3. **Load sample data**: Use `python data_analysis_kit.py` to see analysis examples
4. **Follow the path**: Progress through each day sequentially
5. **Build projects**: Apply learning in mini-projects

---

**Happy Learning! 🚀**

Last Updated: September 2, 2026
