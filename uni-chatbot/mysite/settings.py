"""
Django settings for mysite project.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Get ALLOWED_HOSTS from environment variable
allowed_hosts = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1,::1")
ALLOWED_HOSTS = (
    [host.strip() for host in allowed_hosts.split(",")] if allowed_hosts else []
)

# Security settings - DEVELOPMENT CONFIGURATION
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# SSL/HTTPS settings - DISABLED FOR DEVELOPMENT
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# HSTS settings - DISABLED FOR DEVELOPMENT
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Application definition
INSTALLED_APPS = [
    "mychatbot",
    "users",
    "pages",
    "feedback",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
