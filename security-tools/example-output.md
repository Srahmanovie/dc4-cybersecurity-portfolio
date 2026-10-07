# Example Security Header Analysis

## Target

https://example.com

## Result

```text
~/dc4-cybersecurity-portfolio $ python security-tools/security_headers.py https://example.com

DC4 Security Header Analyzer
========================================
Target: https://example.com/
HTTP Status: 200
Server: cloudflare

Security Headers
----------------------------------------
[-] Content-Security-Policy: MISSING
    Helps control which resources a browser can load.
[-] Strict-Transport-Security: MISSING
    Enforces HTTPS connections.
[-] X-Content-Type-Options: MISSING
    Helps prevent MIME-type sniffing.
[-] X-Frame-Options: MISSING
    Helps protect against clickjacking.
[-] Referrer-Policy: MISSING
    Controls referrer information sent by browsers.
[-] Permissions-Policy: MISSING
    Controls access to selected browser features.

Analysis complete.

Notes
This demonstration was performed against example.com for basic tool validation.
No exploitation or intrusive testing was performed.
