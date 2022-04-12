#! /bin/bash
set -euxo pipefail

export FLASK_APP=minimalcd
export FLASK_DEBUG=1

exec uwsgi --http :80 --workers 1 --threads 2 --wsgi-file minimalcd.wsgi --touch-chain-reload minimalcd.wsgi --chdir /usr/src/app/minimalcd/

