Feature: Task Deletion

    Scenario: Delete an existing task
        Given a user
        And a task "to delete" has been created
        When the user inputs "!delete_task <id>" with the id of the task
        Then the bot outputs "Task with id <id> deleted"
        And the task with that id is deleted
        
