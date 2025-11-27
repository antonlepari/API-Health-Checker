#!/usr/bin/env python3
"""
Simple API Health Checker
Author: Anton Lepari dan ChatGPT
Usage : python3 check_health.py https://example.com/health
"""

import sys
import requests

def check_health(url: str):
    """Check API health by requesting the given URL."""
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

        if status == 200:
            print(f"[OK] {url} is healthy ✔ (HTTP {status})")
        else:
            print(f"[WARN] {url} returned HTTP {status}")
    except requests.exceptions.Timeout:
        print(f"[ERROR] Timeout while connecting to {url}")
    except requests.exceptions.ConnectionError:
        print(f"[ERROR] Cannot connect to {url}")
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_health.py <url>")
        sys.exit(1)

    check_health(sys.argv[1])
