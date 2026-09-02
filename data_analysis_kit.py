"""
Data Analysis Examples for LevelUp Learning Repository.

This module demonstrates common data analysis patterns used throughout
the learning modules.
"""

import pandas as pd
import numpy as np
from typing import Tuple


class DataExplorationKit:
    """Toolkit for data exploration and analysis."""
    
    @staticmethod
    def load_all_datasets() -> dict:
        """Load all available datasets from the datasets folder."""
        datasets = {}
        
        try:
            datasets['titanic'] = pd.read_csv('datasets/titanic.csv')
        except FileNotFoundError:
            print("⚠️  Titanic dataset not found")
        
        try:
            datasets['hr_attrition'] = pd.read_csv(
                'datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv'
            )
        except FileNotFoundError:
            print("⚠️  HR Attrition dataset not found")
        
        return datasets
    
    @staticmethod
    def analyze_missing_data(df: pd.DataFrame) -> pd.DataFrame:
        """Analyze missing data patterns."""
        missing_data = pd.DataFrame({
            'Column': df.columns,
            'Missing_Count': df.isnull().sum(),
            'Missing_Percentage': (df.isnull().sum() / len(df)) * 100
        })
        missing_data = missing_data[missing_data['Missing_Count'] > 0].sort_values(
            'Missing_Percentage', ascending=False
        )
        return missing_data
    
    @staticmethod
    def get_column_types_summary(df: pd.DataFrame) -> dict:
        """Categorize columns by data type."""
        return {
            'numeric': df.select_dtypes(include=[np.number]).columns.tolist(),
            'categorical': df.select_dtypes(include=['object']).columns.tolist(),
            'datetime': df.select_dtypes(include=['datetime64']).columns.tolist(),
            'boolean': df.select_dtypes(include=['bool']).columns.tolist()
        }
    
    @staticmethod
    def get_outliers(df: pd.DataFrame, column: str, method: str = 'iqr') -> Tuple[pd.Series, dict]:
        """Detect outliers using IQR or Z-score method."""
        if method == 'iqr':
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
        else:  # z-score
            z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
            outliers = df[z_scores > 3]
        
        return outliers, {
            'method': method,
            'count': len(outliers),
            'percentage': (len(outliers) / len(df)) * 100
        }
    
    @staticmethod
    def correlation_analysis(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
        """Find top correlations between numeric columns."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        corr_matrix = df[numeric_cols].corr().abs()
        
        # Get upper triangle of correlation matrix
        upper_triangle = corr_matrix.where(
            np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
        )
        
        # Find correlations > 0
        correlations = []
        for column in upper_triangle.columns:
            corr_values = upper_triangle[column]
            correlations.extend([
                {
                    'variable_1': column,
                    'variable_2': index,
                    'correlation': value
                }
                for index, value in corr_values[corr_values > 0].items()
            ])
        
        corr_df = pd.DataFrame(correlations).sort_values(
            'correlation', ascending=False
        )
        
        return corr_df.head(top_n)
    
    @staticmethod
    def distribution_analysis(df: pd.DataFrame) -> dict:
        """Analyze distribution of numeric columns."""
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        analysis = {}
        
        for col in numeric_cols:
            skewness = df[col].skew()
            kurtosis = df[col].kurtosis()
            analysis[col] = {
                'mean': df[col].mean(),
                'median': df[col].median(),
                'std': df[col].std(),
                'skewness': skewness,
                'kurtosis': kurtosis,
                'distribution': 'normal' if abs(skewness) < 0.5 else 'skewed'
            }
        
        return analysis


def demonstrate_analysis():
    """Demonstrate analysis functions with available datasets."""
    print("\n" + "="*70)
    print("LevelUp Data Analysis Toolkit - Demonstration")
    print("="*70)
    
    kit = DataExplorationKit()
    datasets = kit.load_all_datasets()
    
    for dataset_name, df in datasets.items():
        print(f"\n\n{'='*70}")
        print(f"Dataset: {dataset_name.upper()}")
        print(f"{'='*70}")
        
        print(f"\n✓ Shape: {df.shape}")
        
        # Column types
        print(f"\n📊 Column Types Summary:")
        col_types = kit.get_column_types_summary(df)
        for dtype, cols in col_types.items():
            if cols:
                print(f"   {dtype}: {len(cols)} columns")
        
        # Missing data
        print(f"\n⚠️  Missing Data Analysis:")
        missing = kit.analyze_missing_data(df)
        if missing.empty:
            print("   No missing values found!")
        else:
            print(missing.to_string(index=False))
        
        # Correlation analysis (for numeric columns)
        print(f"\n🔗 Top Correlations:")
        try:
            correlations = kit.correlation_analysis(df, top_n=5)
            if not correlations.empty:
                print(correlations.to_string(index=False))
            else:
                print("   No strong correlations found")
        except Exception as e:
            print(f"   Could not compute correlations: {e}")
        
        # Distribution analysis
        print(f"\n📈 Numeric Column Distributions:")
        try:
            distributions = kit.distribution_analysis(df)
            for col, stats in distributions.items():
                print(f"   {col}: {stats['distribution']} (skewness: {stats['skewness']:.2f})")
        except Exception as e:
            print(f"   Could not analyze distributions: {e}")


if __name__ == "__main__":
    demonstrate_analysis()
