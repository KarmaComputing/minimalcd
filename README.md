# Minimal Viable CD

[![Release](https://github.com/KarmaComputing/minimalcd/actions/workflows/release.yml/badge.svg)](https://github.com/KarmaComputing/minimalcd/actions/workflows/release.yml)

- [x] All commits to main branch create a new release automatically

## Local Development

```
cd src
python3.9 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
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
ssh $DOKKU_USERNAME@$DOKKU_SERVER_IP -C dokku builder-dockerfile:set $APP_NAME dockerfile-path src/Dockerfile
git push dokku main
```

### Example:
```
APP_NAME=myapp
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

