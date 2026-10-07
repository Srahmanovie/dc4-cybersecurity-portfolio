Website Security Assessment Methodology

1. Purpose

This methodology describes the process used for authorized web application security assessments.

The objective is to identify security weaknesses, evaluate their potential impact, and provide practical remediation recommendations.

2. Authorization

Security testing is performed only when explicit authorization has been obtained or when the target is an intentionally vulnerable security-training environment.

Before testing a client-owned system, the scope, targets, testing window, permitted techniques, and restrictions should be documented.

3. Scope Definition

The assessment begins by defining the systems that may be tested.

Examples include:

- Web applications
- APIs
- Authentication interfaces
- Public-facing application components
- Authorized supporting infrastructure

Out-of-scope systems are not tested.

4. Reconnaissance

The assessment begins with information gathering relevant to the authorized target.

Activities may include:

- Identifying application functionality
- Mapping publicly exposed application components
- Identifying technologies
- Reviewing application behavior
- Identifying input points
- Mapping the attack surface

Only information relevant to the authorized assessment is collected.

5. Application Mapping

The application's major functionality is documented.

Examples include:

- Login
- Registration
- Search
- Product/category functions
- User profiles
- File upload functionality
- Administrative functionality
- API endpoints

The purpose is to understand where security controls are implemented and where user input enters the application.

6. Security Testing

Testing is performed against the defined scope.

Areas may include:

Authentication

- Authentication controls
- Password policies
- Login protection
- Session handling

Authorization

- Access-control enforcement
- Privilege boundaries
- Horizontal access controls
- Vertical access controls

Input Validation

- Injection vulnerabilities
- Improper validation
- Unsafe processing of user-controlled input

Session Management

- Session handling
- Session expiration
- Cookie security
- Session-related controls

Security Configuration

- Security headers
- TLS configuration
- Information disclosure
- Unnecessary services or functionality

Business Logic

- Workflow manipulation
- Missing security controls
- Abuse of application functionality

7. Finding Validation

Potential vulnerabilities are validated carefully within the authorized scope.

A suspected vulnerability should be confirmed sufficiently to establish:

- The affected component
- The security weakness
- The potential impact
- Reproducibility

Testing should avoid unnecessary damage or exposure of sensitive information.

8. Risk Assessment

Each confirmed finding is assigned a severity based on factors such as:

- Likelihood
- Exploitability
- Required privileges
- Exposure
- Potential business impact
- Confidentiality impact
- Integrity impact
- Availability impact

Typical classifications are:

- Critical
- High
- Medium
- Low
- Informational

9. Evidence Collection

Evidence should demonstrate the finding without unnecessarily exposing sensitive information.

Evidence may include:

- Screenshots
- Sanitized requests/responses
- Relevant application behavior
- Configuration observations
- Reproduction steps

Sensitive credentials, tokens, personal information, and confidential client data should not be included in public portfolios.

10. Reporting

Each finding should contain:

- Finding title
- Severity
- Description
- Affected component
- Evidence
- Impact
- Root cause
- Remediation
- References

The final report should begin with an executive summary suitable for both technical and non-technical stakeholders.

11. Remediation

Recommendations should be practical and prioritized.

Where possible, recommendations should address the underlying root cause rather than only the observed symptom.

12. Retesting

After remediation, the affected functionality should be tested again where authorized.

The objective is to determine whether:

- The vulnerability has been fixed
- The security control is functioning correctly
- The remediation introduced another issue

13. Rules of Engagement

Testing must remain within the agreed scope.

Unless explicitly authorized, testing should not include:

- Denial-of-service activity
- Destructive actions
- Data destruction
- Unauthorized credential attacks
- Access to unrelated systems
- Exfiltration of sensitive information
- Social engineering

14. Responsible Disclosure

Security findings discovered during authorized engagements should be communicated privately to the appropriate system owner.

Public disclosure should occur only when permitted and when it is appropriate to do so.

15. Ethical Standard

The goal of security testing is to help organizations identify and reduce security risk.

Authorization, scope control, confidentiality, minimal-impact testing, and responsible reporting are fundamental requirements of the assessment process.
