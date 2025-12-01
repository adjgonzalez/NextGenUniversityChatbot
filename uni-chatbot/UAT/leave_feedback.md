# UAT: User Leaves Feedback About an Issue

## Scenario: Submit Feedback

- **Given** I am logged in to the website
- **And** I am on the "Feedback" page
- **When** I describe my issue and submit the feedback form
- **Then** I should see a pop up saying "Feedback sent successfully"
- **And** my feedback is recorded for admin review