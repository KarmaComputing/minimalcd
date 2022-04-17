# Minimal Viable Continuous delivery (CD)

> Have you ever wanted to learn Devops, asked "What is Devops" or wanted to start learning DevOps?<br /><br />
This is a minimal viable example of many of the concepts in DevOps which might help you continue to uncover better ways of doing it and help others learn too. <br /><br />Explore this repo, [ask questions](https://github.com/KarmaComputing/minimalcd/discussions/20) and learn

This is a complete web application which:

- [x] ✔️ Automatically generates releases based on semantic version for every merge into the `main` branch (using [intuit/auto](https://github.com/intuit/auto))
- [x] 🗄️ Database migrations are [version controlled](https://github.com/KarmaComputing/minimalcd/tree/main/src/migrations/versions) and ran upon app startup
    - This repository uses [alembic](https://alembic.sqlalchemy.org/en/latest/) (python) but you might use [alembic/doctrine](https://github.com/doctrine/migrations) (php), flyway/liquibase (java) - the concept is the same
- [x] 🔎 When a pull request is opened, a [preview application](https://github.com/KarmaComputing/minimalcd/actions/workflows/pr-preview.yml) is automatically built, with a url so people can view the proposed new version
- [x] 🔃 When a pull request gets merged into the main branch, the latest application is automatically deployed (using [Dokku](https://dokku.com/)). ([Pipeline Code](https://github.com/KarmaComputing/minimalcd/actions/workflows/deploy.yml) / [UI](https://github.com/KarmaComputing/minimalcd/actions/workflows/deploy.yml))
    - You might use Kubernetes with ArgoCD (the underlying concepts are the same)
- [x] 💾 A backup/snapshot of any database is taken pre and post each release
- [x] 🚨 Codebase is regularly automatically scanned for known security issues
- [x] ☸️ At each release a container is built and published to a container registry ([Pipeline Code](https://github.com/KarmaComputing/minimalcd/blob/main/.github/workflows/publish-container.yaml) / [UI](https://github.com/KarmaComputing/minimalcd/actions/workflows/publish-container.yaml))



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

> (almost) Everything below this point are instructions if you wanted to set this up yourself from scratch

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

# Destroy / Teardown everything

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
