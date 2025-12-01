# UAT: User Enrolls in a Program

## Scenario: Program Enrollment

- **Given** I am on the programs page
- **When** I select "Graduate" from the programs list
- **And** I click "MBA" from the expanded list
- **Then** I should be redirected to the MBA program details page
- **When** I click "Apply Now"
- **Then** I should see a pop up saying "Application Successful"
- **And** I receive a confirmation email about my enrollment