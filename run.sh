#!/bin/sh

# Использовать для локального запуска ./run.sh

# Базы
#export DATABASE_URL=postgresql://postgres:375079@localhost:5432/genzis
#export DEV_DATABASE_URL=postgresql://postgres:375079@localhost:5432/genzis

export SECRET_KEY='awEawdae*efsergewr39052jem!sef_efsef,llps'
export CONFIG_NAME=development
export FLASK_APP=backend 
export FLASK_ENV=development

# Миграции
#flask db init
#flask db migrate

flask db upgrade
flask run