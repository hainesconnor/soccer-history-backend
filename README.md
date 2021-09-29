# Soccer History (backend)

## Frontend Link
[Frontend Repo](https://github.com/hainesconnor/soccer-history-frontend)

## Running the project locally
Currently, this project is only setup to run locally. 

First, clone this repo. 

Next, use your preferred package manager to install `pipenv` if you haven't before. (Ex: `pip install pipenv`). 

Next, run `pipenv sync` to install the dependencies from the Pipfile.lock. 

Next, open up a shell with `pipenv shell` and then run `uvicorn app.main:app --reload` to spin up a local backend server. 

By default, the backend server should run at `http://127.0.0.1:8000/`

Once you have the backend setup, then click on the link above for instructions on spinning up the frontend. 

## Backend Design
This API returns historic international soccer match data.

This backend was built with FastAPI, SQLite, and SQLAlchemy. 

To see the available endpoints, checkout the interactive docs at the endpoint `/docs`.  

It also supports user creation, and authentication (although currenlty only a couple endpoints require authentication). 

## Work in Progress
Unittesting, file structure, and a few other odd-and-ends are still WIP. 
