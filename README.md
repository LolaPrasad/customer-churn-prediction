# Customer Churn Prediction & A/B Test Analysis

## Project Overview
This project is an end-to-end data analyst portfolio piece built on the IBM Telco
Customer Churn dataset. It covers the full analytics lifecycle: cleaning and
exploring the data, engineering features, training and comparing four churn
classification models, explaining those predictions with SHAP, scoring the
entire customer base for churn risk, and designing and analysing a simulated
A/B test for a retention discount — finishing with a set of clean CSV exports
ready to plug into Power BI.

## Business Problem
Subscription and telecom businesses lose a significant share of revenue every
year to customer churn, and acquiring a replacement customer is far more
expensive than retaining an existing one. This project answers three practical
questions a retention team would ask: which customers are most likely to
churn and why, how much revenue is at risk from each segment, and whether a
proposed retention discount is actually worth rolling out once its true cost
is accounted for.

## Dataset
- Source: IBM Telco Customer Churn (Kaggle)
- Rows: 7,043 customers (7,032 after cleaning; 11 rows dropped for missing `TotalCharges`)
- Features: 20 input features + 1 target (`Churn`)
- Class imbalance: 26.6% churned, 73.4% retained

## Tools & Libraries
| Category | Tools |
|----------|-------|
| Language | Python 3.x |
| Data manipulation | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Explainability | SHAP |
| Class balancing | Imbalanced-learn (SMOTE) |
| Statistics | SciPy, Statsmodels |
| Model saving | Joblib |
| Dashboard | Power BI |

## Project Structure
```
customer_churn_project/
├── data/
│   ├── raw/                  # Original Kaggle CSV
│   ├── processed/            # Cleaned data + train/test splits
│   └── powerbi/              # Final CSV exports for Power BI
├── models/                   # Saved scaler, feature list, best model
├── outputs/
│   ├── model_comparison.csv
│   ├── shap_feature_importance.csv
│   └── charts/
│       ├── eda/
│       ├── models/
│       ├── shap/
│       ├── risk/
│       └── ab_test/
├── notebooks/
│   ├── 01_data_cleaning_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_shap_explainability.ipynb
│   ├── 05_risk_scoring.ipynb
│   ├── 06_ab_test.ipynb
│   └── 07_powerbi_export.ipynb
├── utils.py                  # Shared helper functions used across notebooks
├── requirements.txt
└── README.md
```

## Key Findings
- Contract length is the single strongest churn driver: month-to-month customers churn at 42.7%, versus 11.3% for one-year and 2.8% for two-year contracts.
- Fiber optic customers churn at 41.9% — more than double the DSL rate — despite being the premium, higher-margin product, pointing to a service-quality or pricing issue worth investigating.
- Electronic check payers churn at 45.3%, far above any other payment method, making autopay migration a promising low-cost retention lever.
- New, higher-paying customers are the highest-risk group: churned customers have a median tenure of just 10 months (vs 38 for retained) and higher monthly charges — an early-life onboarding program would target the biggest source of revenue leakage.
- Service bundling is protective: customers subscribed to 6-8 services churn far less (5-23%) than those with 0 services (43.8%), making cross-selling add-ons (especially OnlineSecurity and TechSupport) a viable retention strategy.

## Model Performance
| Model | Accuracy | Precision | Recall | F1 | AUC |
|-------|----------|-----------|--------|-----|-----|
| Logistic Regression | 0.783 | 0.583 | 0.650 | 0.614 | **0.832** |
| Gradient Boosting | 0.771 | 0.559 | 0.658 | 0.604 | 0.826 |
| XGBoost | 0.757 | 0.539 | 0.594 | 0.565 | 0.819 |
| Random Forest | 0.774 | 0.569 | 0.615 | 0.591 | 0.813 |

Logistic Regression was selected as the best model by AUC — the churn signal in
this dataset is largely linear (driven by contract type, tenure, and charges),
so a well-regularised linear model edges out the tree ensembles here. AUC was
used for model selection specifically because of the ~27% class imbalance,
where accuracy alone would be misleading.

## A/B Test Results
- Control churn rate: 34.6%
- Treatment churn rate: 28.0%
- Result: Statistically significant reduction (p = 0.0244), but the study was underpowered for its own 5pp minimum-detectable-effect target (500 vs. ~1,376 required per group), so the result should be replicated with a larger sample
- Net annual benefit of a **blanket** rollout to all 10,000 high-risk customers: **-£57,134** (a blanket rollout is not profitable — the discount cost on the whole retained base outweighs the revenue saved from the few extra customers kept from churning)
- Recommendation: **Conditional GO** — the discount genuinely reduces churn, but should be rolled out only to customers the churn model flags as **High Risk** (probability ≥ 0.70), not the entire high-risk population, to make the economics work

## How to Run
1. Clone this repository
2. Install requirements: `pip install -r requirements.txt`
3. Place the dataset in `data/raw/` (download `WA_Fn-UseC_-Telco-Customer-Churn.csv` from Kaggle: blastchar/telco-customer-churn)
4. Run notebooks in order: 01 → 02 → 03 → 04 → 05 → 06 → 07
5. Open Power BI and import the CSVs from `data/powerbi/`

## Skills Demonstrated
- Data cleaning & exploratory data analysis
- Feature engineering & preprocessing
- Machine learning (classification)
- Class imbalance handling (SMOTE)
- Model evaluation (AUC, Precision, Recall, F1)
- Model explainability (SHAP values)
- Statistical hypothesis testing (A/B test)
- Power analysis & effect size calculation
- Business communication & stakeholder reporting
- Power BI dashboard design

## Author
**Prasad Lola**
MSc Data Science
University of Essex
[LinkedIn: linkedin.com/in/prasad-lola-517a72240](https://www.linkedin.com/in/prasad-lola-517a72240)
[GitHub: github.com/LolaPrasad](https://github.com/LolaPrasad)
