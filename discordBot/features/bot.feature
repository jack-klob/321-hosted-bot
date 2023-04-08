Feature: Task Creation

    Scenario: Successful task creation
        Given a user
        When the user inputs a command to create a task
        Then the bot responds with a confimation message of the task creation

    Scenario: Task creation no title
        Given a user
        When the user tries to create a task with no title
        Then the bot responds with an error message