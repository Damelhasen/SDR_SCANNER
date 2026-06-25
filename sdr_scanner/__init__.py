"""sdr_scanner package

Expose a tiny API and package version.
"""

__version__ = "0.1.0"

from .core import scan

__all__ = ["scan"]
