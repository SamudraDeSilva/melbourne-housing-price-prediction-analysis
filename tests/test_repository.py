"""Offline, standard-library checks for the public GitHub publication package."""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / 'notebooks' / 'Melbourne_Housing_Price_Prediction.ipynb'

class TestPublicationIntegrity(unittest.TestCase):
    def test_notebook_structure_and_cached_execution(self):
        with NOTEBOOK.open(encoding='utf-8') as handle:
            nb = json.load(handle)
        cells = nb['cells']
        self.assertEqual(len(cells), 269)
        self.assertEqual(sum(c['cell_type'] == 'code' for c in cells), 143)
        self.assertEqual(sum(c['cell_type'] == 'markdown' for c in cells), 126)
        self.assertEqual(
            sum(o.get('output_type') == 'error' for c in cells for o in c.get('outputs', [])), 0)

    def test_documentation_and_history(self):
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        changelog = (ROOT / 'CHANGELOG.md').read_text(encoding='utf-8')
        for value in ('January', 'June 2023', 'November 2026'):
            self.assertIn(value, readme)
            self.assertIn(value, changelog)
        for name in ('MODEL_CARD.md', 'VERIFICATION.md', 'model_metrics.csv',
                     'VALIDATION_SUMMARY.json', 'requirements.txt', 'data/README.md'):
            self.assertTrue((ROOT / name).is_file(), name)
            self.assertIn(name, readme)

    def test_machine_readable_metrics(self):
        summary = json.loads((ROOT / 'VALIDATION_SUMMARY.json').read_text(encoding='utf-8'))
        with (ROOT / 'model_metrics.csv').open(encoding='utf-8', newline='') as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), len(summary['cv_results']))
        winners = [r for r in rows if r['Selected_for_holdout'] == 'Yes']
        self.assertEqual(len(winners), 1)
        winner = winners[0]
        self.assertEqual(winner['Model'], summary['metrics']['model'])
        self.assertAlmostEqual(float(winner['Holdout_R2']), float(summary['metrics']['r2']), places=4)
        self.assertAlmostEqual(float(winner['Holdout_RMSE_AUD']), float(summary['metrics']['rmse'].replace(',', '')), places=2)
        self.assertAlmostEqual(float(winner['Holdout_MAE_AUD']), float(summary['metrics']['mae'].replace(',', '')), places=2)
        for row in rows:
            cv = summary['cv_results'][row['Model']]
            self.assertAlmostEqual(float(row['CV_R2']), cv[0], places=3)
            self.assertAlmostEqual(float(row['CV_RMSE_AUD']), cv[1], places=3)
            self.assertAlmostEqual(float(row['CV_MAE_AUD']), cv[2], places=3)
        card = (ROOT / 'MODEL_CARD.md').read_text(encoding='utf-8')
        for metric in ('0.8174', '269,347.86', '172,488.79'):
            self.assertIn(metric, card)

    def test_visual_assets_exist(self):
        for filename in ('melbourne_project_cover.png', 'model_comparison.png',
                         'geographical_price_distribution.png', 'price_distribution.png',
                         'regional_property_comparison.png'):
            self.assertTrue((ROOT / 'images' / filename).is_file(), filename)

if __name__ == '__main__':
    unittest.main()
