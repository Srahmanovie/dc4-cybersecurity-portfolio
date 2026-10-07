#!/usr/bin/env python3

import sys
import requests


SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps control which resources a browser can load.",
    "Strict-Transport-Security": "Enforces HTTPS connections.",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing.",
    "X-Frame-Options": "Helps protect against clickjacking.",
    "Referrer-Policy": "Controls referrer information sent by browsers.",
    "Permissions-Policy": "Controls access to selected browser features.",
}


def analyze_headers(url):
    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            headers={"User-Agent": "DC4-Security-Header-Analyzer/1.0"},
        )
    except requests.RequestException as error:
        print(f"[!] Request failed: {error}")
        return

    print("\nDC4 Security Header Analyzer")
    print("=" * 40)
    print(f"Target: {response.url}")
    print(f"HTTP Status: {response.status_code}")
    print(f"Server: {response.headers.get('Server', 'Not disclosed')}")
    print("\nSecurity Headers")
    print("-" * 40)

    for header, description in SECURITY_HEADERS.items():
        if header in response.headers:
            print(f"[+] {header}: PRESENT")
        else:
            print(f"[-] {header}: MISSING")
        print(f"    {description}")

    print("\nAnalysis complete.")


def main():
    if len(sys.argv) != 2:
        print("Usage: python security_headers.py https://example.com")
        sys.exit(1)

    url = sys.argv[1]

    if not url.startswith(("http://", "https://")):
        print("[!] Please provide a complete URL.")
        sys.exit(1)

    analyze_headers(url)


if __name__ == "__main__":
    main()
