# NextGen University Chatbot

This project aims to create a website that contains education programs that a student can enroll into. The student will be aided by a chatbot that can interact with the user through conversation or predefined paths, it supports 450~ intents across different languages at various stages of their time as a student and will perform different tasks depending on user input, ranging from page redirection and admin contact to the delivery of program material via email.

# Version: Iteration 4

As of Iteration 4, our website and chatbot have received a better look through the revamped UI. The Chatbot is now a chatbot proper through the addition of intent recognition, it's now powered by a list of more than 450 intents meant to support different languages and our CI pipeline is in full effect.

# Prerequisites

 \- Python 3.12 (IMPORTANT!!!, Django has compability issues with Python 3.14+)

 \- pip (Python package manager)

 \- Git

 \- A Clone of the repository
```
git clone https://github.com/adjgonzalez/NextGenUniversityChatbot/
```

# Quick Start setup sequence:

```
# 1. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Navigate to Django project root (where manage.py is)
cd uni-chatbot

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install pre-commit hooks
pip install pre-commit

# 5. Generate environment file
python -c "import secrets; key = secrets.token_urlsafe(50); open('.env', 'w', encoding='utf-8').write(f'DEBUG=True\nSECRET_KEY={key}\nALLOWED_HOSTS=localhost,127.0.0.1,::1')"

# 6. Set up database
python manage.py migrate

# 7. Load fixtures (baseline data)
python manage.py loaddata fixtures/pages_data.json

# 8. Install Playwright
pip install pytest-playwright
npx playwright install --with-deps
playwright install

# 9. Create superuser (follow prompts)
python manage.py createsuperuser

# 10. Run development server
python manage.py runserver
```
# Installation \& Setup

# 1\. Create and Activate Virtual Environment

Windows:

```

# python -m venv venv

# venv\\Scripts\\activate

```

macOS/Linux:

```

# python3 -m venv venv

# source venv/bin/activate

```

# 2\. Install Dependencies

```

# pip install -r requirements.txt

```

# 3\. Environment Configuration

Our Ethereal email features use specific credentials in the .env file, otherwise we print the sent email to terminal.

# 4\. Database Setup

```
python manage.py makemigrations
```

# Apply migrations
```
# python manage.py migrate
```

# Load Base Data
```
# python manage.py loaddata pages_data.json
```
Load Seed Data to populate application

# 5\. Create Superuser (Admin Account)

```
# python manage.py createsuperuser
```
Follow the prompts to create an admin account for accessing the Django admin panel.

# 6\.Run the Development Server

```
# python manage.py runserver
```

Visit http://localhost:8000 in your browser.

# Testing the Application

For testing, the Playwright tests NEED the localhost server to be running so a 2nd terminal running the python manage.py runserver command while the 1st is running the Playwright tests is needed.

- Run the module Unit Tests (These run in the uni-chatbot directory)

```
# python manage.py test
```
- Run the Integration Tests (These run in the uni-chatbot directory)

```
python manage.py test -v 2 integration_tests
```

- Run the Chatbot intent Unit Test (This is one of the main tests, it's located in uni-chatbot/chatbot_browser_tests)

```
# python chatbot_browser_tests/chatbot_intent_test.py
```
- Run the E2E smoke test (This is another important test, it's located in uni-chatbot/system_tests)

```
python system_tests/e2e_tests.py
```

# Access Points

- Homepage: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/ (use superuser credentials)
- Admissions: http://127.0.0.1:8000/admissions/ (This redirects to http://127.0.0.1:8000/admissions/undergraduate/ as a landing page for Admissions)
- Undergraduate: http://127.0.0.1:8000/admissions/undergraduate/
- Graduate: http://127.0.0.1:8000/admissions/graduate/
- Online Courses: http://127.0.0.1:8000/admissions/online_course/
- Funding & Scholarships: http://127.0.0.1:8000/admissions/funding/
- Contact: http://127.0.0.1:8000/contact/
- Feedback: http://127.0.0.1:8000/feedback/
- User Registration: http://127.0.0.1:8000/users/register/
- User Login: http://127.0.0.1:8000/users/login/
- Password Reset: http://127.0.0.1:8000/password_reset/
- Password Reset: Done: http://127.0.0.1:8000/password_reset/done/
  
# Project Structure
```
NextGenUniversityChatbot/
├── .github/                     # GitHub workflows, CI, nightly build
├── docs/                        # Project documentation and artifacts
├── UAT/                         # User Acceptance Test scenarios
└── uni-chatbot/                 # DJANGO PROJECT ROOT
    ├── feedback/                # Django app for feedback submission and storage
    ├── chatbot_browser_tests/   # Playwright-based chatbot intent unit test
    ├── integration_tests/       # Django integration tests (test interactions between components/apps)
    ├── system_tests/            # End-to-end and system-level tests for the entire application
    ├── regression_test_nightly  # Contains the regression test we run on the nightly build at 3 AM
    ├── fixtures/                # Database and app fixtures for populating test data
    ├── mychatbot/               # Core chatbot functionality Django app
    ├── mysite/                  # Django project configuration and settings (settings.py)
    ├── pages/                   # Django app for website pages (content, structure, navigation)
    ├── users/                   # Django app for user accounts, authentication, and user management
```
# Code Quality & Development Tools

This project uses automated code formatting and linting (Black and Ruff).

# Pre-commit Hooks
Install pre-commit (one-time setup)
```
pip install pre-commit
pre-commit install
```
# Run on all files (optional)
```
pre-commit run --all-files

# Auto-format code
black .

# Check code style
ruff check .

# Fix auto-fixable issues
ruff check --fix .
```
# Troubleshooting and common issues

- "CommandError: You must set settings.ALLOWED\_HOSTS if DEBUG is False"
```
Solution: Ensure .env file exists with DEBUG=True and ALLOWED\_HOSTS set
```
- Google Translate banner
```
Solution: Run python manage.py compilemessages for each language
```
- Pages not loading errors
```
Solution: Run the fixtures to get the baseline data our program needs: python manage.py loaddata fixtures/pages_data.json
```
- Module not found errors
```
Solution: Ensure virtual environment is activated and run pip install -r requirements.txt
```
- One of the test is not running
```
Solution: Ensure you're in the right folder. Running python manage.py tests won't pull all the tests, there are specific instructions above on how to reach each one.
```
