# GitHubAPI

## Intro

The purpose of this repository is to hold the content for a technical challenge requested by Captalys' team.

Technologies:
- Python 3.7
  - Flask
  - Flask-restx
- [Docker-compose](https://docs.docker.com/compose/)

PS: The reason for Flask-restx is that flask-restplus is deprecated

## Project structure

```
- githubapi
  - src
    - api
      - api.py              -- Base class for all API's based objects
      - github_api.py       -- Consumer of the GitHub's API
    - model
      - user.py             -- Model containing the definitions of user data
    - views
      - user.py             -- Endpoints available for retrieving data from GitHub's API through this app
    - app.py                -- Python script to start the server and its dependencies
  - tests
    - model
      - test_model_user.py  -- Test file containing tests for the User model
    - views
      - test_view_user.py   -- Test file containing tests for the endpoints
```

## Setup

There are just two steps in order to have the app ready

```shell script
$ docker-compose build
$ docker-compose up -d
```

As soon as the command finishes the app will be accessible through the URL `http://0.0.0.0:8181`.
A Swagger UI should be visible with the following endpoints:

- /users/{username} - Get all public repos from a specific user
- /users/{username}/{repo_name} - Get repo details from a specific user

PS: All endpoints should be consumed using the GET HTTP verb


## Marcelo Aquino - 2020
