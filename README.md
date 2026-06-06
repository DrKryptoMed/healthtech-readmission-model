# 30-Day Hospital Readmission Risk Model

## Overview
A machine learning system that predicts 30-day hospital readmission 
risk at the point of patient discharge. Built on synthetic clinical 
data from Synthea, following production ML engineering standards.

## Clinical Context
Hospital readmissions within 30 days represent a significant quality 
and cost burden on health systems. This model enables care teams to 
identify high-risk patients at discharge for targeted intervention —
arranging follow-up, adjusting medications, or flagging for a 
social worker.

## Project Structure
- `data/raw/` — original Synthea output, never modified
- `data/interim/` — partially cleaned data
- `data/processed/` — final feature matrix for ML
- `notebooks/` — exploratory analysis
- `src/` — production Python code
- `models/` — saved model artifacts
- `reports/` — evaluation reports and figures

## Setup
```bash
conda create -n readmission-env python=3.11
conda activate readmission-env
conda install -c conda-forge setuptools -y
pip install -r requirements.txt
```

## Known Issues
- pkg_resources requires: `conda install -c conda-forge setuptools`
  before `pip install -r requirements.txt` on Windows

## Status
✅ Environment setup
✅ Data exploration
✅ Feature engineering
✅ Model training (XGBoost AUC 0.891)
✅ FastAPI serving (3 endpoints, 5.4ms response)
✅ Docker containerisation
🚧 Clinical dashboard frontend (next)