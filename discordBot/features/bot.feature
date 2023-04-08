Feature: Testing workflow secret

    Scenario: Testing workflow secrets
        Given the secret
        When the test bot tries to send a command
        Then the command is sent