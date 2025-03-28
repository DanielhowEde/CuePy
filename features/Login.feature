Feature: Login Test

Scenario: Valid Login
Given I navigate to the Login page
When I enter "test" into the username field
And I enter "test" into the password field
Then User is taken to homepage
