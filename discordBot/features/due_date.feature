Feature: Due Date

    Scenario: Correctly setting a due date
        Given a user
        And an id for a created task
        When the user inputs <!due_date <id> "2023-04-06 12:15"> with the id of a task
        Then the bot outputs "Task <id> due date set to **2023-04-06 12:15**"

    Scenario: Setting a due date with incorrect format
        Given a user
        And an id for a created task
        When the user inputs <!due_date <id> "12:15 2023/04/06"> with the id of a task
        Then the bot outputs "Due date must be in format YYYY-MM-DD HH:MM"
