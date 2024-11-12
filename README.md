# DevOps Apprenticeship: Project Exercise

> If you are using GitPod for the project exercise (i.e. you cannot use your local machine) then you'll want to launch a VM using the [following link](https://gitpod.io/#https://github.com/CorndelWithSoftwire/DevOps-Course-Starter). Note this VM comes pre-setup with Python & Poetry pre-installed.

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.8+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

You can check poetry is installed by running `poetry --version` from a terminal.

**Please note that after installing poetry you may need to restart VSCode and any terminals you are running before poetry will be recognised.**

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/2.3.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.


## Setting up Trello
You need a Trello account for this application. Once you have setup an account and a board you will need to setup an API Key and Token and add them to the `.env` file.

Furthermore, you will need to add the board id and the "Todo" and "Done" column/list ids (i.e. you need to choose which you're using and which columns count as "Todo" and "Done" for item statuses).

## Running the App locally 

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app 'todo_app/app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-666-066
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Running the test suite
To run the tests for the codebase run the following command:

poetry run pytest

(please make sure you have run 'poetry install' beforehand to instal pytest)

## Deploiyng the app via ansible 
TO deploy the application via ansible copy the 'ansible' folder to the host node, update the inventory file (to include the control nodes you'd like to deploy to)and run the following command:
ansible-playbook playbook.yaml -i inventory.yaml

Please note you will need to have set up passwordless SSH access from the host to each of the managed nodes

## building and running the app via docker
To build the container for local development, please run 
~~~bash
docker build --tag todo-app:dev --target development .
~~~
to run the container for local development please run
~~~
docker run --publish 8000:5000 -it --env-file .env   --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:dev
~~~

For the production container the build and run commands are:-
~~~ bash
docker build --tag todo-app:prod --target production .

docker run --publish 8000:5000 -it --env-file .env   --mount "type=bind,source=$(pwd)/todo_app,target=/app/todo_app" todo-app:prod