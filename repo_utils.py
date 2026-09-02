"""
Utility functions for the LevelUp Data Science Learning Repository.

This module provides tools for:
- Repository structure analysis
- Dataset loading and exploration
- Learning progress tracking
"""

import os
import json
from pathlib import Path
from typing import Dict, List, Optional
import pandas as pd


class LevelUpRepoAnalyzer:
    """Analyzer for the LevelUp data science learning repository."""
    
    def __init__(self, repo_path: str = "."):
        """Initialize the repository analyzer."""
        self.repo_path = Path(repo_path)
        self.notebooks = self._find_notebooks()
        self.datasets = self._find_datasets()
        self.markdown_files = self._find_markdown_files()
    
    def _find_notebooks(self) -> List[Path]:
        """Find all Jupyter notebooks in the repository."""
        return sorted(self.repo_path.glob("*.ipynb"))
    
    def _find_datasets(self) -> Dict[str, Path]:
        """Find all dataset files in the datasets directory."""
        datasets = {}
        dataset_dir = self.repo_path / "datasets"
        if dataset_dir.exists():
            for csv_file in dataset_dir.glob("*.csv"):
                datasets[csv_file.stem] = csv_file
        return datasets
    
    def _find_markdown_files(self) -> List[Path]:
        """Find all markdown documentation files."""
        return sorted(self.repo_path.glob("*.md"))
    
    def print_repo_structure(self) -> None:
        """Print a formatted view of the repository structure."""
        print("\n" + "="*60)
        print("LevelUp Repository Structure")
        print("="*60)
        
        print("\n📚 LEARNING MODULES (Jupyter Notebooks):")
        for i, nb in enumerate(self.notebooks, 1):
            print(f"   {i}. {nb.name}")
        
        print("\n📊 DATASETS:")
        for name, path in self.datasets.items():
            size_kb = path.stat().st_size / 1024
            print(f"   • {name} ({size_kb:.1f} KB)")
        
        print("\n📖 DOCUMENTATION:")
        for doc in self.markdown_files:
            if doc.name != "README.md":  # Skip README
                print(f"   • {doc.name}")
        
        print("\n" + "="*60 + "\n")
    
    def get_dataset_summary(self, dataset_name: str) -> Optional[pd.DataFrame]:
        """Load and display summary statistics for a dataset."""
        if dataset_name not in self.datasets:
            print(f"Dataset '{dataset_name}' not found.")
            return None
        
        df = pd.read_csv(self.datasets[dataset_name])
        
        print(f"\n{'='*60}")
        print(f"Dataset: {dataset_name}")
        print(f"{'='*60}")
        print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        print(f"\nColumn Information:")
        print(df.info())
        print(f"\nFirst few rows:")
        print(df.head())
        print(f"\nBasic Statistics:")
        print(df.describe())
        
        return df
    
    def list_learning_path(self) -> None:
        """Display the learning path sequence."""
        print("\n" + "="*60)
        print("Suggested Learning Path")
        print("="*60)
        
        path_sequence = [
            ("Day 01", "Pandas Basics", "Learn fundamental pandas operations"),
            ("Day 02", "Data Cleaning", "Handle missing data and data preparation"),
            ("Day 04", "Statistics", "Statistical analysis and hypothesis testing"),
            ("Day 06", "Scikit-learn", "Introduction to machine learning"),
        ]
        
        for day, topic, description in path_sequence:
            print(f"\n{day}: {topic}")
            print(f"   → {description}")
            
            # Find corresponding notebook
            for nb in self.notebooks:
                if topic.lower().replace("-", "_").replace(" ", "_") in nb.name.lower():
                    print(f"   📓 {nb.name}")


def load_titanic_dataset() -> pd.DataFrame:
    """Load the Titanic dataset."""
    return pd.read_csv("datasets/titanic.csv")


def load_hr_attrition_dataset() -> pd.DataFrame:
    """Load the HR Employee Attrition dataset."""
    return pd.read_csv("datasets/WA_Fn-UseC_-HR-Employee-Attrition.csv")


def quick_eda(df: pd.DataFrame, name: str = "Dataset") -> None:
    """Perform quick exploratory data analysis on a dataframe."""
    print(f"\n{'='*60}")
    print(f"Quick EDA: {name}")
    print(f"{'='*60}")
    
    print(f"\nDataset Shape: {df.shape}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nBasic Statistics:\n{df.describe()}")
    print(f"\nNumerical Columns: {len(df.select_dtypes(include=['number']).columns)}")
    print(f"Categorical Columns: {len(df.select_dtypes(include=['object']).columns)}")


if __name__ == "__main__":
    # Initialize the analyzer
    analyzer = LevelUpRepoAnalyzer(".")
    
    # Display repository structure
    analyzer.print_repo_structure()
    
    # Display learning path
    analyzer.list_learning_path()
    
    # Load and summarize datasets
    print("\n" + "="*60)
    print("Dataset Summaries")
    print("="*60)
    
    for dataset_name in analyzer.datasets.keys():
        try:
            df = analyzer.get_dataset_summary(dataset_name)
        except Exception as e:
            print(f"Error loading {dataset_name}: {e}")
