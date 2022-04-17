# Minimal Viable CD

[![Release](https://github.com/KarmaComputing/minimalcd/actions/workflows/release.yml/badge.svg)](https://github.com/KarmaComputing/minimalcd/actions/workflows/release.yml)

- [x] All commits to main branch create a new release automatically
- [x] Database migrations are version controlled and ran upon app startup
- [x] When a pull request gets merged into the main branch, the latest application is deployed
- [x] A backup/snapshot of any database is taken pre and post each release
- [x] Codebase is regularly automatically scanned for known security issues

## Local Development

```
cd src
python3.9 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
 ```

Env settings:
```
cp .env.example .env
```

### Run locally
```
cd src
. venv/bin/activate
export FLASK_APP=minimalcd
export FLASK_DEBUG=1
flask run
```
http://127.0.0.1:5000

## Build
```
podman build -t minimalcd -f src/Dockerfile
```

## Run
```
podman run -p 8082:80 minimalcd
```

# Day0

### Dokku

```
APP_NAME=<app-name>
DOKKU_SERVER_IP=<dokku-server-ip>
DOKKU_USERNAME=<username>
git remote add dokku $DOKKU_USERNAME@$DOKKU_SERVER_IP:$APP_NAME
git remote -v show
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku apps:create $APP_NAME
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku git:initialize $APP_NAME
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku builder:set minimalcd build-dir src
git push dokku main
```

### Example:
```
APP_NAME=minimalcd
DOKKU_SERVER_IP=192.168.1.10
DOKKU_USERNAME=dokku
git remote add dokku $DOKKU_USERNAME@$DOKKU_SERVER_IP:$APP_NAME
git remote -v show
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku apps:create $APP_NAME
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku git:initialize $APP_NAME
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku builder-dockerfile:set $APP_NAME dockerfile-path src/Dockerfile
git push dokku main
```

### Auto release using autoc

```
curl -L https://github.com/intuit/auto/releases/download/v10.36.5/auto-linux.gz > auto-linux.gz
gunzip auto-linux.gz
chmod +x auto-linux
./auto-linux init
# follow on-screen
./auto-linux create-labels
```

# Destory / Teardown everything

```
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku apps:destroy --force $APP_NAME
```

#### Troubleshooting

Dokku by default expects your `Dockerfile` to be in the root directory, **and**
the default working directory is the root of the repo.

For changing the name/location of the Dockerfile, you can use the `builder-dockerfile:set`:
```
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku builder-dockerfile:set $APP_NAME dockerfile-path Dockerfile
```
For changing the working directory of the `docker build` context, use:
```
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku builder:set minimalcd build-dir src
```
See https://github.com/dokku/dokku/pull/4502 for more details.
