# Release verification — Melbourne Housing Price Prediction

## Release scope

The public repository package was checked against the previously validated November 2026 Melbourne project release. This documentation alignment **does not modify or re-execute the Jupyter Notebook**.

| Check | Recorded result |
|---|---|
| Jupyter Notebook | `notebooks/Melbourne_Housing_Price_Prediction.ipynb` |
| Original cell count retained | **269** |
| Code cells / Markdown cells | **143 / 126** |
| Saved notebook error outputs | **0** |
| Dataset used in prior full execution | **13,580 rows × 21 columns** |
| Prior reported full execution | **143 / 143 code cells completed without errors** |
| Original project period | **January–June 2023** |
| Technical revision and GitHub preparation | **November 2026** |
| Current test-set R² | **0.8174** |
| Current test-set RMSE | **A$269,347.86** |
| Current test-set MAE | **A$172,488.79** |

The train-only five-fold CV selection and held-out evaluation details are documented in [`MODEL_CARD.md`](MODEL_CARD.md). The numerical values in `MODEL_CARD.md`, `model_metrics.csv`, `VALIDATION_SUMMARY.json` and README match the notebook's saved result table.

## How to verify the publication package

Run from the repository root:

```bash
python -m unittest discover -s tests -v
```

The offline tests check notebook structure, cached execution errors, date attribution, documented result consistency, visual assets and optional dataset schema (when `data/melb_data.csv` is present). **These tests do not retrain the models.** For a full scientific reproduction, install dependencies, download the original dataset and run all 143 code cells as instructed in the README.

## Data and provenance

The full source CSV is **excluded** from the public package. Instructions for obtaining it, including the dataset's attribution and licence, are in [`data/README.md`](data/README.md).

## Authorship

The original notebook structure and contributor references are preserved. Verify and credit any collaborators before public release.
