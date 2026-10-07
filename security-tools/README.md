DC4 Security Header Analyzer

A lightweight Python tool for reviewing common HTTP security headers.

Purpose

The tool checks whether selected security-related HTTP response headers are present on an authorized web target.

It is intended for:

- Security assessments
- Defensive security reviews
- Cybersecurity education
- Security configuration analysis

Headers Checked

The tool currently checks:

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

Requirements

- Python 3
- "requests"

Install the dependency:

pip install requests

Usage

python security_headers.py https://example.com

Replace the URL with a website you own or have explicit authorization to assess.

Example Output

DC4 Security Header Analyzer
========================================
Target: https://example.com
HTTP Status: 200
Server: Example

Security Headers
----------------------------------------
[+] Content-Security-Policy: PRESENT
[-] Strict-Transport-Security: MISSING
[+] X-Content-Type-Options: PRESENT
[+] X-Frame-Options: PRESENT
[-] Referrer-Policy: MISSING
[+] Permissions-Policy: PRESENT

Analysis complete.

Responsible Use

Only use this tool against systems that you own, intentionally vulnerable training environments, or systems for which you have explicit authorization.

The tool performs HTTP requests and should not be used to scan systems without permission.

Future Improvements

Planned improvements include:

- JSON output
- CSV reporting
- TLS configuration checks
- Cookie security analysis
- Configurable header checks
- Risk scoring
- HTML report generation
