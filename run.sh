#!/bin/sh

#export DB_TYPE=postgresql
#export DB_USER=postgres
#export DB_PASSWORD=375079
#export DB_NAME=genzis
#export DB_HOST=localhost
#export DB_PORT=5432
export SECRET_KEY='awEawdae*efsergewr39052jem!sef_efsef,llps'
#export DATABASE_URL=postgresql://postgres:375079@localhost:5432/genzis
#export DEV_DATABASE_URL=postgresql://postgres:375079@localhost:5432/genzis
export CONFIG_NAME=development
export FLASK_APP=backend 
export FLASK_ENV=development
#flask db init
#flask db migrate
flask db upgrade
flask run