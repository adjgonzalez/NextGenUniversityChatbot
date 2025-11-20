# \# NextGen University Chatbot

# This project aims to create a website that contains education programs that a student can enroll into. The student will be aided by a chatbot at various stages of their time as a student and will perform different tasks depending on user input, ranging from page redirection and feedback collection to the delivery of program material via email.

# Version: Iteration 3

# As of Iteration 3, our pages are now dynamically populated and localized in 3 different languages, we also support the enrollment of new students. 

# Prerequisites

# \- Python 3.8+

# \- pip (Python package manager)

# \- Git

# Installation \& Setup

# 1. Clone the Repository

```

# git clone https://github.com/adjgonzalez/NextGenUniversityChatbot/

```

# 2\. Create and Activate Virtual Environment

# Windows:

```

# python -m venv venv

# venv\\Scripts\\activate

```

# macOS/Linux:

```

# python3 -m venv venv

# source venv/bin/activate

```

# 3\. Install Dependencies

```

# pip install -r requirements.txt

```

# 4\. Environment Configuration

# Create a .env file in the project root (same directory as manage.py):

# .env file
```
# DEBUG=True

# SECRET\_KEY=

# ALLOWED\_HOSTS=localhost,127.0.0.1,::1

# Important: Generate a secure secret key:

# python -c "from django.core.management.utils import get\_random\_secret\_key; print(get\_random\_secret\_key())"
```

# 5\. Database Setup


```
# python manage.py makemigrations
```
# 

# \# Apply migrations
```
# python manage.py migrate
```
# 6\. Create Superuser (Admin Account)

```
# python manage.py createsuperuser
```
# Follow the prompts to create an admin account for accessing the Django admin panel.

# 7\. Set Up Translations

# Extract translation strings:

```
# python manage.py makemessages -l es  # Spanish

# python manage.py makemessages -l fr  # French
```

# Compile translations:

# 

```
# python manage.py compilemessages -l es
# python manage.py compilemessages -l fr  
```
# 8\. Collect Static Files

```
# python manage.py collectstatic
```

# 9\. Run the Development Server

```
# python manage.py runserver
```

# Visit http://localhost:8000 in your browser.

# Testing the Application

# Run Unit Tests

```
# python manage.py test
```

# Access Points

# Homepage: http://localhost:8000/

# Admin Panel: http://localhost:8000/admin/ (use superuser credentials)


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
# Development Workflow

# Adding New Translations

# Extract strings from code:

# 

```
# python manage.py makemessages -l <language\_code>
```
# Edit the .po file in locale/<language\_code>/LC\_MESSAGES/django.po

# Compile translations:

```
# python manage.py compilemessages -l <language\_code>
```
# Database Changes

# When modifying models:

# python manage.py makemigrations

# python manage.py migrate

# Adding New Dependencies

# Install package:

# pip install <package-name>

# Update requirements:

```
# pip freeze > requirements.txt
```

# Troubleshooting

# Common Issues

# "CommandError: You must set settings.ALLOWED\_HOSTS if DEBUG is False"
```
Solution: Ensure .env file exists with DEBUG=True and ALLOWED\_HOSTS set
```
# Translations not showing
```
Solution: Run python manage.py compilemessages for each language
```
# Static files not loading
```
Solution: Run python manage.py collectstatic
```
# Database errors
```
Solution: Run python manage.py migrate to apply migrations
```
# Module not found errors
```
Solution: Ensure virtual environment is activated and run pip install -r requirements.txt
```
# Quick Start Commands Summary

# For easy copy-pasting, here's the essential setup sequence:

```
# 1. Clone the repository

# git clone https://github.com/adjgonzalez/NextGenUniversityChatbot/

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Navigate to Django project root (where manage.py is)
cd uni-chatbot

# 4. Install dependencies
pip install -r requirements.txt

# 5. Generate environment file
python -c "import secrets; key = secrets.token_urlsafe(50); open('.env', 'w', encoding='utf-8').write(f'DEBUG=True\nSECRET_KEY={key}\nALLOWED_HOSTS=localhost,127.0.0.1,::1')"

# 6. Set up database
python manage.py migrate

# 7. Create superuser (follow prompts)
python manage.py createsuperuser

# 8. Set up translations
python manage.py makemessages -l es -l fr
python manage.py compilemessages -l es -l fr

# 9. Collect static files
python manage.py collectstatic --noinput

# 10. Run development server
python manage.py runserver