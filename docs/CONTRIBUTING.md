# Contributing Guide
This guide will help you get started with development and ensure consistent code quality.

# Development Setup
# 1. Fork and Clone
Fork the repository on GitHub, then:
git clone https://github.com/your-username/university-chatbot-project
cd university-chatbot-project
# 2. Environment Setup

# Install dependencies
```
pip install -r requirements.txt
```
# Set up environment variables (if testing Ethereal)
```
cp .env.example .env
```
Edit .env with your settings
# 3. Database Setup
```
python manage.py migrate
python manage.py createsuperuser  # If needed for admin access
```
# 4. Load fixtures (baseline data)
```
python manage.py loaddata fixtures/pages_data.json
```
# 4. Code Quality Setup
# Install pre-commit hooks (automatically formats code before commits)
```
pre-commit install
```
# Development Workflow
# 1. Create a Feature Branch

git checkout -b feature/your-feature-name or git checkout -b fix/issue-description
# 2. Make Your Changes

- Write clear, focused commits
- Follow the existing code style
- Add tests for new functionality

# 3. Test Your Changes
Run the test suite
```
python manage.py test
```
# 4. Ensure Code Quality
# Format code automatically
```
black.
```
# Lint and auto-fix issues
```
ruff check --fix .
```
# Run pre-commit checks on all files
```
pre-commit run --all-files
```
# 5. Commit Your Changes
Use conventional commit format (see below).

# 6. Push and Create Pull Request
```
git push origin your-branch-name
```
Then create a Pull Request on GitHub.

Commit Message Convention
We follow Conventional Commits for clear, standardized commit messages.
```
Format:
type(scope): description
[optional body]
[optional footer]
```
# Types or scopes:
```
feat: New features or functionality
fix: Bug fixes
docs: Documentation updates
style: Code style changes (formatting, missing semi-colons, etc.)
refactor: Code refactoring (no behavior change)
test: Test additions or modifications
chore: Maintenance tasks, dependency updates
ci: CI configuration changes
perf: Performance improvements
security: Security-related changes
```
Examples:
```
feat: add user authentication system
fix: resolve chatbot response timeout issue
docs: update API endpoint documentation
style: format code with Black
refactor: simplify chatbot response logic
test: add unit tests for admission views
chore: update Django to latest patch version
Scopes (optional):
auth: Authentication related
chatbot: Chatbot functionality
ui: User interface
api: API endpoints
db: Database related
```
# Pull Request Process
1. Ensure tests pass - All existing and new tests should pass

2. Update documentation - If you change functionality, update relevant docs

3. Follow code style - Use Black and Ruff formatting

4. Add descriptive title - Clear summary of changes

5. Provide context - Explain what and why you're changing

# Code Review Checklist
Before submitting a PR, ensure:

- Functionality
- Tests are added/updated

- All tests pass

- No breaking changes introduced

- Manual testing completed

# Code Quality
Code follows PEP 8 and project style guide

- No security issues introduced
- Error handling is appropriate
- Code is documented where necessary

# Documentation
- README update if needed
- API documentation updated
- Comments added for complex logic

# Issue creation
- Check existing issues and PRs before creating new ones
- Use clear, descriptive titles for issues
- Provide reproduction steps for bugs

# Security
- Never commit secrets or sensitive data
- Use environment variables for configuration
- Report security vulnerabilities privately to maintainers
