# Architecture Overview
This document serves as a template designed for a rapid and comprehensive understanding of the codebase's architecture, enabling efficient navigation and effective contribution. Update this document as the codebase evolves.

## 1. Project Structure
This section provides a high-level overview of the project's directory and file structure, categorised by architectural layer or major functional area. It is essential for quickly navigating the codebase, locating relevant files, and understanding the overall organization and separation of concerns.


[uni-chatbot]/
├── mychatbot/                       # Contains all server-side code and APIs
│   ├── migrations/                  # Main source code for backend services
│   │   └── __init__.py/             #
│   ├── static/                      # Frontend configuration files
│   │  ├── images/                   # Frontend configuration files
│   │  │  ├── group.png              # Frontend configuration files
│   │  │  ├── logo.png               # Frontend configuration files
│   │  │  └── logo1.png              # Frontend configuration files
│   │  ├── js/                       # Backend unit
│   │  │  ├── admission_sidebar.js   # Backend unit
│   │  │  ├── chatbox.png            # Backend unit
│   │  │  └── navbar.png             # Backend unit
│   │  ├── mychatbot/                # Backend unit
│   │  │  ├── admissions.png         # Frontend configuration files
│   │  │  ├── pages.png              # Frontend configuration files
│   │  │  └── style.png              # Frontend configuration files
│   ├── __init__.py                  # Backend unit
│   ├── admin.py                     # Backend unit
│   ├── apps.py                      # Backend unit
│   ├── models.py                    # Backend unit
│   ├── tests.py                     # Backend unit and unit test
│   ├── urls.py                      # Backend unit
│   └── views.py                     # Backend unit
├── mysite/                          # Contains all client-side code for user interfaces
│   ├── __init__.py                  # Main source code for frontend applications
│   ├── asgi.py                      # Main source code for frontend applications
│   ├── settings.py                  # Main source code for frontend applications
│   ├── urls.py                      # Main source code for frontend applications
│   └── wsgu.py                      # Main source code for frontend applications
├── pages/                           # Main source code for frontend applications
│   ├── migrations/                  # Main source code for frontend applications
│   │  ├── 0001_initial.py           # Main source code for frontend applications
│   │  └── __init__.py               # Main source code for frontend applications
│   └── templates/                   # Main source code for frontend applications
│   │  ├── admissions/               # Main source code for frontend applications
│   │  │  ├── admission.html         # Frontend configuration files
│   │  │  ├── funding.html           # Frontend configuration files
│   │  │  ├── graduate.html          # Frontend configuration files
│   │  │  ├── online_course.html     # Frontend configuration files
│   │  │  ├── siderbar.html          # Frontend configuration files
│   │  │  └── undergraduate.html     # Frontend configuration files
│   │  ├── base/                     # Frontend configuration files
│   │  │  ├── base.html              # Frontend configuration files
│   │  │  ├── chatbox.html           # Frontend configuration files
│   │  │  ├── contact.html           # Frontend configuration files
│   │  │  ├── faculty.html           # Frontend configuration files
│   │  │  ├── footer.html            # Frontend configuration files
│   │  │  ├── navbar.html            # Frontend configuration files
│   │  │  ├── programs.html          # Frontend configuration files
│   │  │  └── programs_detail1.html  # Frontend configuration files
│   │  ├── pages/                    # Frontend configuration files
│   │  │  └── home.html              # Frontend configuration files
│   │  ├── __init__.py               # Main source code for frontend applications
│   │  ├── admin.py                  # Main source code for frontend applications
│   │  ├── apps.py                   # Main source code for frontend applications
│   │  ├── models.py                 # Main source code for frontend applications
│   │  ├── tests.py                  # Main source code for frontend applications
│   │  ├── urls.py                   # Main source code for frontend applications
│   │  └── views.py                  # Main source code for frontend applications
├── users/                           # Main source code for frontend applications
│   ├── migrations/                  # Main source code for frontend applications
│   │  ├── 0001_initial.py           # Main source code for frontend applications
│   │  └── __init__.py               # Main source code for frontend applications
│   ├── templates/users/             # Frontend configuration files
│   │  ├── login.html                # Frontend configuration files
│   │  └── register.html             # Frontend configuration files
│   manage.py                        # Main source code for frontend applications
│   pyproject.toml                   # General utility functions
│   superuser.json                   # General utility functions
├── .gitignore                       # General utility functions
├── .pre-commit-config.yaml          # General utility functions
├── LICENSE                          # General utility functions
├── NextGenUseCase.png               # General utility functions
├── README.md                        # Project overview and quick start guide
├── requirements.txt                 # Specifies intentionally untracked files to ignore
└── ARCHITECTURE.md                  # This document


## 2. High-Level System Diagram
The project’s objective is to create a website that’ll allow a prospective student to find a program of their liking in our University’s website via website navigation or the help of a chatbot. We aim to assist the student in their initial process of enrolling and adjusting to university life so we will send useful resources to the student depending on their enrolled program upon registration and upon request to the chatbot. We will also implement a localization feature that will translate the entire website (including the chatbot) to different languages and a feedback feature where the student can communicate issues and comments directly to the admins.

[User] <--> [Frontend Application] <--> [Backend Service 1] <--> [Database 1]
                                    |
                                    +--> [Backend Service 2] <--> [External API]

## 3. Core Components

### 3.1. Frontend

Website - A centralized web platform that presents all academic programs offered by a university.

Chatbot - An interactive chatbot designed to guide the student to a program appropriate to their preferences.

User enrollment - An account management that includes student registration (sign-up), login (sign-in) and password recovery.

User Feedback System

### 3.2. Backend Services

Localization - Students can select their preferred interface language.

Feedback Mechanism - The system will include a feature that allows students to provide feedback on the enrollment process.

Chat Transcript - Students can choose to receive a transcript of the chat they were just in.

Database - Structured and secure database for storing user’s information, ensuring integrity and only accessed by authorized staff.

Resource Delivery - Upon successful registration, the system will deliver automatically via email useful resources such as admission requirements and application process steps.

Unit testing - A specific test performed to each module in the system.

Integration testing - A test perform between modules than work together.

System testing - A complet test of all the modules that conform the system.

## 4. Data Stores

Structured and secure database for storing user’s information, ensuring integrity and only accessed by authorized staff.

## 5. External Integrations / APIs

(List any third-party services or external APIs the system interacts with.)

Service Name 1: [e.g., Stripe, SendGrid, Google Maps API]

Purpose: [Briefly describe its function, e.g., "Payment processing."]

Integration Method: [e.g., REST API, SDK]

## 6. Deployment & Infrastructure

Cloud Provider: [e.g., AWS, GCP, Azure, On-premise]

Key Services Used: [e.g., EC2, Lambda, S3, RDS, Kubernetes, Cloud Functions, App Engine]

CI/CD Pipeline: [e.g., GitHub Actions, GitLab CI, Jenkins, CircleCI]

Monitoring & Logging: [e.g., Prometheus, Grafana, CloudWatch, Stackdriver, ELK Stack]

## 7. Security Considerations

(Highlight any critical security aspects, authentication mechanisms, or data encryption practices.)

Authentication: [e.g., OAuth2, JWT, API Keys]

Authorization: [e.g., RBAC, ACLs]

Data Encryption: [e.g., TLS in transit, AES-256 at rest]

Key Security Tools/Practices: [e.g., WAF, regular security audits]

## 8. Development & Testing Environment

Local Setup Instructions: [Link to CONTRIBUTING.md or brief steps]

Testing Frameworks: [e.g., Jest, Pytest, JUnit]

Code Quality Tools: [e.g., ESLint, Black, SonarQube]

## 9. Future Considerations / Roadmap

(Briefly note any known architectural debts, planned major changes, or significant future features that might impact the architecture.)

[e.g., "Migrate from monolith to microservices."]

[e.g., "Implement event-driven architecture for real-time updates."]

## 10. Project Identification

Project Name: University Enrollment System

Repository URL: http://127.0.0.1:8000/

Primary Contact/Team: Arnoldo Gonzalez

Date of Last Update: [2025-11-13]
