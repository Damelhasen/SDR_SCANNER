import json

from sdr_scanner.core import write


def test_write_and_read(tmp_path):
	temp_scan = {"100.0": -10.5, "101.0": -20.0}
	file_path = tmp_path / "scanned_frequencies.json"
	write(str(file_path), json.dumps(temp_scan, indent=2))

	with open(file_path, "r", encoding="utf-8") as f:
		data = json.load(f)

	assert data == temp_scan