#! /bin/bash
set -euxo pipefail

export FLASK_APP=minimalcd
export FLASK_DEBUG=1

if [ -a .env ]
then
  echo ".env exists already so not copying from .env.example"
else
  echo ".env not found, so copying from .env.example"
  cp .env.example .env
fi

exec uwsgi --http :80 --workers 1 --threads 2 --wsgi-file minimalcd.wsgi --touch-chain-reload minimalcd.wsgi --chdir /usr/src/app/minimalcd/

