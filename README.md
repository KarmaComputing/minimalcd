# Minimal Viable CD


## Build
```
podman build -t minimalcd -f src/Dockerfile
```

## Run
```
podman run -p 8082:80 minimalcd
```