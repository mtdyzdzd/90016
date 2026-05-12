# Sprint 2 US-09 Role Registration Verification - 12 May 2026

## Purpose

This evidence note records the final Sprint 2 verification for `US-09`: new users can register with a selected university outreach officer or university student role/classification.

## Implementation Configuration

| Area | Verified Configuration |
| ---- | ---------------------- |
| Registration page | Public registration page is available at `/register/`. |
| Form plugin | The registration form is implemented through Forminator (`User Registration`, form ID 69). |
| Required fields | Username, email, password, and user type. |
| User type options | University student; University outreach officer. |
| Role records | WordPress roles exist for `University Student` and `University Outreach Officer`. |
| Login protection | Force Login continues to redirect unauthenticated access to the protected site. |
| Registration bypass | `/register/` is allowed through Force Login so unauthenticated users can create accounts. |
| Legacy registration routes | WordPress native register links and `/local-signup/` redirect to `/register/`. |

## Verification Steps

| Step | Result |
| ---- | ------ |
| Request the protected home page while logged out. | Redirected to the WordPress login page. |
| Request `/register/` while logged out. | Registration page returned successfully and displayed the Forminator registration form. |
| Inspect the registration form. | Username, email, password, and required user type fields were visible. |
| Inspect user type options. | Both University student and University outreach officer were available. |
| Register a temporary test user. | Temporary user `graycat` was created successfully through the public registration page. |
| Check the created user in the WordPress user list. | `graycat` was listed with the `University Student` role. |
| Log in with the temporary user. | The user reached the protected Sprint 2 school outreach map page. |

## Acceptance Result

`US-09` is accepted on 12 May 2026. Registration is no longer treated as disabled or blocked. The verified student-role path and the configured outreach-officer option satisfy the Sprint 2 role-registration requirement at the current level of role-based behaviour needed before Sprint 3.
