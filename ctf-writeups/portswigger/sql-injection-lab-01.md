SQL Injection Lab 01 — Beginner Writeup

1. Overview

- Platform: PortSwigger Web Security Academy
- Category: Web Application Security
- Vulnerability: SQL Injection (SQLi)
- Difficulty: Beginner
- Environment: Authorized training lab
- Status: Completed

2. Objective

Understand how SQL injection occurs when an application handles user input unsafely in database queries.

3. Vulnerability Description

SQL injection is a web application vulnerability in which user-controlled input can interfere with SQL query logic. Depending on the vulnerable query and database permissions, this may expose information, bypass authentication, or allow unauthorized data modification.

4. Methodology

1. Opened an intentionally vulnerable training lab.
2. Observed the application's normal behavior.
3. Identified the relevant input and response.
4. Tested the input within the authorized lab.
5. Compared the response with normal behavior.
6. Confirmed that the lab's success condition was met.
7. Documented the potential impact and remediation.

5. Finding

Finding: Unsafe handling of user-controlled input in a database query.

Root cause: SQL queries may be constructed by combining SQL instructions with untrusted input instead of separating query logic from data.

Potential impact: Depending on the application's implementation, SQL injection can result in unauthorized data access, authentication bypass, or modification of records.

6. Recommended Remediation

- Use parameterized queries or prepared statements.
- Avoid concatenating untrusted input into SQL statements.
- Apply least-privilege permissions to database accounts.
- Validate input according to application requirements.
- Return safe error messages without exposing database details.
- Add automated security tests for database-related input handling.

7. Evidence

Suggested evidence files:

- "01-baseline.png"
- "02-lab-completed.png"

Only publish screenshots that you have captured yourself. Remove session cookies, credentials, personal information, and unique lab access details before uploading.

8. Lessons Learned

- User-controlled input can affect database query behavior.
- Application responses can help identify security weaknesses.
- Good reports explain the vulnerability, impact, and remediation.
- Parameterized queries are a primary defense against SQL injection.
- Testing must remain within authorized environments.

9. Responsible Testing

This exercise was conducted in an authorized training environment. Never test systems without permission and a clearly defined scope.

10. References

- PortSwigger Web Security Academy — SQL Injection: https://portswigger.net/web-security/sql-injection
- OWASP SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html

---

Author: DC4 Cybersecurity
Purpose: Cybersecurity learning and portfolio development
