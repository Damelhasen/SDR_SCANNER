# SDR Scanner

Lightweight SDR scanning utilities and helpers for RTL-SDR and compatible devices.

## Installation

```bash
pip install .
```

## Usage

```python
from sdr_scanner import write

# Example: write scan data to a JSON file
write("scan.json", "{\"100.0\": -10.5}")
```

## Packaging

This project is configured for PyPI upload using `pyproject.toml` and `setuptools`.

## Files included for PyPI

- `pyproject.toml`
- `README.md`
- `LICENSE`
- `sdr_scanner/`

## Requirements

The package depends on:

- `numpy`
- `matplotlib`
- `pyrtlsdr`
