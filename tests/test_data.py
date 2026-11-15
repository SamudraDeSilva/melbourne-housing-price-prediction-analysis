"""Optional source-data checks; skip when the licensed dataset is not downloaded."""
import csv
import unittest
from pathlib import Path

CSV = Path(__file__).resolve().parents[1] / 'data' / 'melb_data.csv'

@unittest.skipUnless(CSV.is_file(), 'Source CSV not bundled: download data/melb_data.csv as explained in data/README.md')
class TestSourceData(unittest.TestCase):
    def test_melbourne_housing_snapshot_shape_and_target(self):
        with CSV.open(encoding='utf-8-sig', newline='') as handle:
            reader = csv.DictReader(handle)
            self.assertEqual(len(reader.fieldnames or []), 21)
            self.assertTrue({'Price','Rooms','Type','Suburb','Date'}.issubset(reader.fieldnames or []))
            self.assertEqual(sum(1 for _ in reader), 13_580)

if __name__ == '__main__':
    unittest.main()
