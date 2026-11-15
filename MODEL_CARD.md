# Model Card — Melbourne Housing Price Prediction

## Purpose and status

This is an **educational, historical price-regression study**. It investigates recorded Melbourne house-sale prices, not live property valuations or prospective sales prices. The original project was developed **January–June 2023**; the reproducible modelling and reporting workflow was technically revised in **November 2026**.

It is **not intended for mortgage lending, automated financial decisions, or current property valuation** without substantial additional validation, data updates and governance.

## Data

- **Dataset:** Melbourne Housing Snapshot (`melb_data.csv`), 13,580 historical records with 21 original variables.
- **Transaction period:** January 2016–September 2017.
- **Target:** `Price`, observed transaction price, Australian dollars (AUD).
- **Inputs:** Numeric housing and geographic attributes and the `Council` categorical feature. The '+ Type' variants additionally encode the property `Type` category. Feature lists are defined explicitly in the notebook.
- **Source and redistribution:** See [`data/README.md`](data/README.md). The licensed CSV is intentionally **not included** in this GitHub package.

## Modelling and evaluation

- **Train/test partition:** 80% training (**10,864 records**) and 20% held-out test (**2,716 records**), shuffled with `random_state=42`.
- **Model selection:** Training-only, shuffled **five-fold K-Fold cross-validation**, selecting the model with the lowest mean CV RMSE.
- **Pipeline preprocessing:** Numeric missing-value imputation and categorical one-hot encoding occur inside cross-validation folds, using training data only. The SVR comparison uses a scalable `LinearSVR` setup.
- **Candidates:** Linear Regression, LinearSVR, XGBoost, Linear Regression + Type, and XGBoost + Type.
- **Final evaluation:** The selected candidate is evaluated once on the held-out test partition; a mean-price baseline provides context.

## Five-fold training cross-validation

| Model | Mean R² | Mean RMSE (AUD) | Mean MAE (AUD) |
|---|---:|---:|---:|
| **XGBoost + Type** | **0.796** | **288,815** | **173,923** |
| XGBoost | 0.775 | 303,010 | 185,278 |
| Linear Regression + Type | 0.573 | 417,504 | 260,467 |
| Linear Support Vector Regression | 0.524 | 439,712 | 274,174 |
| Linear Regression | 0.524 | 439,714 | 274,181 |

## Selected model: held-out test metrics

| Metric | Value |
|---|---:|
| Selected model | **XGBoost + Type** |
| Test R² | **0.8174** |
| Test RMSE | **A$269,347.86** |
| Test MAE | **A$172,488.79** |
| Mean-price baseline test RMSE | **A$630,259.30** |

Training CV and held-out test metrics should **not be treated interchangeably**. For machine-readable values, see [`model_metrics.csv`](model_metrics.csv) and [`VALIDATION_SUMMARY.json`](VALIDATION_SUMMARY.json). The final test metrics reflect the **2026 revised evaluation**, not the original 2023 results.

## Limitations and appropriate interpretation

- The data are historical and may no longer represent current Melbourne market conditions.
- Randomly splitting historical records does **not** establish accuracy for future sale dates; chronological or out-of-period validation is needed for genuine forecasting.
- Rare expensive properties, missing construction or area attributes, and potentially inaccurate source records can produce high error on individual sales.
- Address and higher-cardinality location attributes were not fully exploited; other features may omit relevant market effects.
- No independent external dataset, comprehensive hyperparameter search, model calibration, deployment validation or uncertainty intervals are provided.
- Feature associations should **not** be interpreted as causal claims.

## Reproducibility

See the [README](README.md) for setup and the notebook's complete methodology. The CSV is downloaded separately from Kaggle as documented in [`data/README.md`](data/README.md). Repository consistency checks: `python -m unittest discover -s tests -v`. A full notebook re-execution additionally requires the dataset and installed dependencies.
