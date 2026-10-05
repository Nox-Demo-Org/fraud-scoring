"""Calls the external fraud data vendor.

The call has no timeout. During the vendor's slowdown on 2026-08-27 every request waited until
the vendor answered, and claim registration stalled for 47 minutes (see #tw-architecture).
"""

import os

import requests

VENDOR_URL = os.getenv("FRAUD_VENDOR_URL", "https://vendor.example/score")


def vendor_score(customer_id: str, peril: str) -> float:
    res = requests.post(VENDOR_URL, json={"subject": customer_id, "peril": peril})
    return float(res.json().get("risk", 0.0))
