# Project history and reproducibility notes

## Original development — January to June 2023

- The original Melbourne Housing Price Prediction study was undertaken during **January–June 2023**.
- The initial project explored property prices using the historical Melbourne housing snapshot, descriptive visualisation and regression modelling.
- The detailed, long-form notebook and its original section structure are retained for publication.
- This entry records the user-provided original project period; it does **not** imply that the 2026 reworked model evaluation was performed in 2023.

## Technical revision and GitHub publication - November 2026

This edition is a **technical correction, not a condensed rewrite**. It retains all 269 cells, in their original order, from the Melbourne housing notebook.

## Execution

- Clean run verified using the supplied 13,580-row CSV and a Python 3.13 environment.
- All 143 executable cells completed without error.
- Results are freshly saved in the notebook.

## Analysis

- Fixed CSV loading, numeric-only pandas aggregations and correlation calculations.
- Repaired dummy encoding and concatenation and NaN-safe outlier detection.
- Preserved descriptive analyses while separating predictive modelling from all-data EDA transformations.
- Address-specific suspected erroneous measurements are documented, with implausible year values treated as missing for modelling.
- Replaced an unnecessarily expensive, numerically unscaled SVR with scaled LinearSVR.
- Introduced training-only five-fold CV with fold-local imputation and encoding.
- Added a baseline comparison and final hold-out metrics without repeatedly evaluating model candidates on test data.
- Updated Plotly map calls to current, supported syntax.

## Caution

The corrected regression results are intentionally **not identical** to previously cached results; those earlier metrics were generated under a different data-cleaning and evaluation procedure. The original manuscript is not represented as a new peer-reviewed publication.

## Final publication audit (15 November 2026)

- Preserved all 269 original cells and original visual presentation.
- Fixed pandas deprecation warnings and robust dataset lookup.
- Executed all 143 code cells against the provided CSV without errors.
- Updated conclusion and README to match the verified run: R² = 0.8174, RMSE = A$269,347.86, MAE = A$172,488.79.
- Excluded the licensed CSV from the GitHub pack; see data/README.md.
