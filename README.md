A discord bot to help with task management

# Build
A build file has been provided to allow for easy building of the project

1. In the terminal make sure you are in the main directory (project-bot8) then enter
```
./build_file.sh
```

2. If you run into a permission error enter this command then repeat step 1
```
chmod +x build_file.sh 
```
Running the build script will also trigger the tests.

# Testing

When in the `discordBot` directory, tests are executed using the command:
```
python manage.py test
```
Coverage reports are generated to the terminal using `django-nose`.

