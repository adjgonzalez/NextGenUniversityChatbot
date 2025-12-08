# Architecture Overview
This document serves as a template designed for a rapid and comprehensive understanding of the codebase's architecture, enabling efficient navigation and effective contribution. Update this document as the codebase evolves.

## 1. Project Structure
This section provides a high-level overview of the project's directory and file structure, categorised by architectural layer or major functional area. It is essential for quickly navigating the codebase, locating relevant files, and understanding the overall organization and separation of concerns.

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
