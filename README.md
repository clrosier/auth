# Auth

The intention of this flask application is to provide a REST api which will support authentication for a front-end 
and eventually a mobile app for managing exercise.  This is mostly a personal use project but it does contain the capability for others to use just by signing up.

## Running the api
This application is meant to run as a Docker container and eventually will be optimized for deployment on k8s.

For now it's possible to run as a standalone container like so:

### Option 1: Build from source
```bash
# Grab source code
git clone https://github.com/clrosier/auth.git

# Build the docker image
docker build -t auth .


# Run the image as a container
docker run -d \
    --rm \
    --name auth \
    -p 5000:5000 \
    -e AUTH_DB_URL=ip_of_postgres_db \
    -e AUTH_DB_USER=my-user \
    -e AUTH_DB_PASS=my-admin-password \
    -e AUTH_DB_PORT=5432 \
    auth
```

### Option 2: Pull from Dockerhub
```bash
# Grab simage
docker pull clrosier/auth

# Run the image as a container
docker run -d \
    --rm \
    --name auth \
    -p 5000:5000 \
    -e AUTH_DB_URL=ip_of_postgres_db \
    -e AUTH_DB_USER=my-user \
    -e AUTH_DB_PASS=my-admin-password \
    -e AUTH_DB_PORT=5432 \
    auth
```
