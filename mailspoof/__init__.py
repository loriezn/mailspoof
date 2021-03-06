"""Scans SPF and DMARC records for issues that could allow email spoofing."""

from .scanners import SPFScan, DMARCScan, Scan, scan
from .cli import __version__
