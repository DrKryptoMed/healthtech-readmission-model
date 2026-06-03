"""
Setup verification script.
Run this to confirm environment and data are ready for Lesson 2.
"""
import sys
import os
import pandas as pd
import numpy as np
import sklearn
import xgboost
import mlflow
import shap


def check_packages():
    print("=" * 40)
    print("PACKAGE VERSIONS")
    print("=" * 40)
    print(f"Python:       {sys.version.split()[0]}")
    print(f"Pandas:       {pd.__version__}")
    print(f"NumPy:        {np.__version__}")
    print(f"Scikit-learn: {sklearn.__version__}")
    print(f"XGBoost:      {xgboost.__version__}")
    print(f"MLflow:       {mlflow.__version__}")
    print(f"SHAP:         {shap.__version__}")
    print()


def check_structure():
    print("=" * 40)
    print("PROJECT STRUCTURE")
    print("=" * 40)
    expected_dirs = [
        "data/raw",
        "data/processed",
        "data/interim",
        "notebooks",
        "src",
        "models",
        "reports"
    ]
    all_good = True
    for d in expected_dirs:
        exists = os.path.isdir(d)
        status = "✓" if exists else "✗"
        print(f"  {status} {d}/")
        if not exists:
            all_good = False
    print()
    return all_good


def check_data():
    print("=" * 40)
    print("SYNTHEA DATA FILES")
    print("=" * 40)
    data_path = "data/raw/output/csv"

    if not os.path.exists(data_path):
        print("  ✗ Data folder not found. Run Synthea first.")
        print()
        return False

    expected_files = [
        "patients.csv",
        "encounters.csv",
        "conditions.csv",
        "medications.csv",
        "observations.csv",
        "procedures.csv",
    ]

    all_good = True
    for fname in expected_files:
        fpath = os.path.join(data_path, fname)
        if os.path.exists(fpath):
            df = pd.read_csv(fpath)
            print(f"  ✓ {fname}: {len(df):,} rows × {len(df.columns)} cols")
        else:
            print(f"  ✗ {fname}: NOT FOUND")
            all_good = False
    print()
    return all_good


if __name__ == "__main__":
    check_packages()
    struct_ok = check_structure()
    data_ok = check_data()

    if struct_ok and data_ok:
        print("✅ All checks passed — ready for Lesson 2")
    else:
        print("❌ Fix the issues above before proceeding")