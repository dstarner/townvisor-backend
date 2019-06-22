# Townvisor Backend REST API

This is the Django REST API that manages and controls Townvisor, the next generation 
of travel blogging.

## Getting Started

Follow the guides below to get started in development.

### Getting the Environment Set Up

1. Createh virtual environment. We use the `venv` module, because it is built in and requires no external dependencies.
    ```bash
    python3 -m venv venv
    ````
2. And then we can activate that environment.
   ```bash
   source venv/bin/activate
   # On Fish shell
   source venv/bin/activate.fish
   ```
3. And install our dependencies
   ```bash
   pip install -r requirements.txt
   ```

### Database Control

To create and manage the database, run the following two commands.

```bash
./manage.py makemigrations
./manage.py migrate
```

### Start the server

To start the server, run the following and visit `127.0.0.1:8000/docs` in your browser.

```bash
./manage.py runserver
```