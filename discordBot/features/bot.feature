Feature: Task Creation

    Scenario: Successful task Creation
        Given a user
        When the user inputs a command to create a task
        Then the bot responds with a confimation message of the task creation