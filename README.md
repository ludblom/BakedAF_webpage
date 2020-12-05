# BakedAF Webpage
Just a simple webpage planned for us to spend our time at. The reason because most other webpages suck and/or are too heavy.

## Installation
Have to install these dependencies

`pip install flask flask-sqlalchemy flask-login`

## Setup for debugging
`export FLASK_APP=project`

`export FLASK_DEBUG=1`

## Initialize a database for testing purposes
`from project import db, create_app`

`db.create_all(app=create_app())`

## Running test server
Run `flask run`
