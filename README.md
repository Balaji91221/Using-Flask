# Flask + Firebase · Authentication Prototype

A small learning project connecting an HTML form to a Flask route and a Firebase authentication client.

## Purpose

This repository explores the request path behind an authentication form: the browser submits fields, Flask reads the form values, and a Python adapter calls Firebase. It is an early prototype with known setup and API-method gaps.

## Included files

| File | Responsibility |
|---|---|
| [`Testing/app.py`](Testing/app.py) | Flask app, form route, and Firebase adapter setup |
| [`Testing/templates/new.html`](Testing/templates/new.html) | Form and feedback display |
| [`Testing/templates/new.css`](Testing/templates/new.css) | Form styling |
| [`requirements.txt`](requirements.txt) | Incomplete original dependency list |

## Request flow

```text
Browser form → Flask GET/POST route → Pyrebase authentication client
                              └──→ rendered success/error message
```

## Setup status

The current requirements file lists only `requests`; it does not declare the Flask and Pyrebase packages imported by the application. The repository also includes an old Windows virtual environment, which should not be treated as a portable installation.

Use a fresh Python virtual environment and provide compatible Flask and Pyrebase4 dependencies. The checked-in environment identifies Flask 2.2.2 and Pyrebase4 4.5.0, but a complete reproducible dependency set has not been supplied.

Before trying the form:

1. Configure a Firebase project you control and enable the intended email/password authentication flow.
2. Replace the embedded Firebase project configuration in `Testing/app.py` with your own configuration.
3. Correct the route's `sign_up_with_email_and_password` call: the included Pyrebase4 adapter exposes `create_user_with_email_and_password` for registration and `sign_in_with_email_and_password` for sign-in. Choose the intended behavior and matching UI copy.

After the dependencies and integration are configured, the application entry point is:

```bash
cd Testing
python app.py
```

## Current boundaries

The form displays login-oriented messages, while the handler attempts a signup operation. No authenticated session, protected pages, or logout flow is implemented. The entry point enables Flask debug mode and is intended for local development.
