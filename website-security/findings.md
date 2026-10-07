Finding 01 — SQL Injection

Overview

During an authorized security assessment of an intentionally vulnerable web application provided by PortSwigger Web Security Academy, a SQL injection vulnerability was identified in an application input parameter.

The vulnerability allowed the application's database query to be manipulated through user-controlled input.

Severity

High

«Severity is contextual. The final rating for a real engagement should consider the specific application's exposure, privileges, data sensitivity, and exploitability.»

Testing Environment

Target: PortSwigger Web Security Academy lab

Testing authorization: Intentionally vulnerable training environment

Testing type: Web application security assessment

Vulnerability Description

SQL injection occurs when an application incorporates untrusted user input into a database query without adequate validation or parameterization.

An attacker may potentially manipulate the intended database query and cause the application to perform unintended database operations.

Assessment Methodology

The assessment followed these stages:

1. Reviewed the application's normal behavior.
2. Identified user-controlled input associated with the vulnerable functionality.
3. Tested how the application processed modified input.
4. Observed the application's response.
5. Confirmed the vulnerability within the authorized laboratory environment.
6. Documented the security impact and recommended remediation.

Evidence

Evidence was collected from the authorized training laboratory.

Screenshots:

- "01-baseline.png" — Normal application behavior

- "02-lab-solved.png" — Successful lab completion


Sensitive session information and unique laboratory identifiers should be removed before public publication.

Potential Impact

Depending on the application's database privileges and implementation, SQL injection can potentially result in:

- Unauthorized access to database information
- Authentication bypass
- Modification of application data
- Loss of data integrity
- Disclosure of sensitive information
- Further compromise of the application

The actual impact must be evaluated against the specific application and database configuration.

Root Cause

The underlying issue is typically caused by constructing database queries using untrusted input rather than safely separating application data from SQL instructions.

Remediation

Recommended controls include:

1. Use parameterized queries/prepared statements.
2. Avoid dynamically constructing SQL statements from untrusted input.
3. Apply appropriate server-side input validation.
4. Use least-privilege database accounts.
5. Implement secure error handling that does not expose database information.
6. Conduct security testing during development and before deployment.
7. Monitor application and database logs for suspicious activity.

Secure Development Recommendation

The preferred defense is parameterized database access.

Application developers should ensure that user-controlled values are passed as data parameters rather than concatenated into SQL statements.

Lessons Learned

This assessment demonstrated the importance of:

- Identifying user-controlled input
- Understanding application/database interaction
- Validating suspected vulnerabilities
- Assessing business impact
- Documenting findings clearly
- Providing actionable remediation guidance

Authorization and Ethics

Testing was performed only against an intentionally vulnerable training environment.

No unauthorized systems were tested.

References

- OWASP — SQL Injection
- PortSwigger Web Security Academy — SQL Injection
