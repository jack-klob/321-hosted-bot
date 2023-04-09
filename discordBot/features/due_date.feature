Feature: Due Date

    Scenario: Correctly setting a due date
        Given a user
        And an id for a created task
        When the user inputs <!due_date <id> "2023-04-06 12:15"> with the id of a task
        Then the bot responds with "Task <id> due date set to **2023-04-06 12:15**"