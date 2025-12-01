# UAT: User is Redirected by Chatbot Navigation

## Scenario: Navigate to Program Page via Chatbot

- **Given** I am using the chatbot
- **When** I click "No" on the "Are you already a student?" question
- **And** I select "Graduate" from the options provided by the chatbot
- **And** I click "MBA" from the graduate programs list in the chatbot
- **Then** the assistant should say "Taking you to the MBA page..."
- **And** I should be automatically redirected to the MBA program details page (`/programs/mba/`)