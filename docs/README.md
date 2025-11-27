# NextGen University Chatbot

This project aims to create a website that contains education programs that a student can enroll into. The student will be aided by a chatbot at various stages of their time as a student and will perform different tasks depending on user input, ranging from page redirection and feedback collection to the delivery of program material via email.

# Version: Iteration 3

As of Iteration 3, our pages are now dynamically populated and localized in 3 different languages, we also support the enrollment of new students.

# Prerequisites

 \- Python 3.8+

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

# 7. Create superuser (follow prompts)
python manage.py createsuperuser

# 8. Set up translations
python manage.py makemessages -l es -l fr
python manage.py compilemessages -l es -l fr

# 9. Run development server
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

Create a .env file in the project root (same directory as manage.py):

# .env file
```
# DEBUG=True

# SECRET\_KEY=

# ALLOWED\_HOSTS=localhost,127.0.0.1,::1

# Important: Generate a secure secret key:

# python -c "from django.core.management.utils import get\_random\_secret\_key; print(get\_random\_secret\_key())"
```

# 4\. Database Setup


```
python manage.py makemigrations
```

# Apply migrations
```
# python manage.py migrate
```
# 5\. Create Superuser (Admin Account)

```
# python manage.py createsuperuser
```
Follow the prompts to create an admin account for accessing the Django admin panel.

# 6\. Set Up Translations

Extract translation strings:

```
# python manage.py makemessages -l es  # Spanish

# python manage.py makemessages -l fr  # French
```

# Compile translations:

```
# python manage.py compilemessages -l es
# python manage.py compilemessages -l fr
```
# 7\.Run the Development Server

```
# python manage.py runserver
```

Visit http://localhost:8000 in your browser.

# Testing the Application

- Run Unit Tests

```
# python manage.py test
```

# Access Points

- Homepage: http://localhost:8000/

- Admin Panel: http://localhost:8000/admin/ (use superuser credentials)

# Project Structure
```
NextGenUniversityChatbot/
├── uni-chatbot/             # DJANGO PROJECT ROOT
│   ├── feedback/            # Feedback system app
│   ├── locale/              # Translation files (i18n)
│   ├── mychatbot/           # Chatbot application
│   ├── mysite/              # Django project settings
│   ├── pages/               # Static pages app
│   ├── tests/               # Test files
│   ├── test_results/        # Test output/results
│   ├── users/               # User authentication & management
│   ├── manage.py            # Django management script
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
└── venv/                    # Python virtual environment
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
- Translations not showing
```
Solution: Run python manage.py compilemessages for each language
```
- Database errors
```
Solution: Run python manage.py migrate to apply migrations
```
- Module not found errors
```
Solution: Ensure virtual environment is activated and run pip install -r requirements.txt
```
