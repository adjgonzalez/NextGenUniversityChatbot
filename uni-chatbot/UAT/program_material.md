# UAT: User Receives Program Material via Email

## Scenario: Request Program Material

- **Given** I am using the chatbot
- **When** I click on "Yes" on the "Are you already a student?" question
- **Then** I click on "Email my program resources"
- **Then** I request program material for "MBA" and provide my email address
- **Then** the assistant should say "Program resources sent to your email!"
- **Then** I receive an email containing the material for "MBA"