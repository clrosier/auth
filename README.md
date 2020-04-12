# bills-api

The intention of this flask application is to provide a REST api which will support a fron-end
and eventually a mobile app for tracking bills and expenses.  This is mostly a personal use project but it does contain the capability for others to use just by signing up.

## Running the api
This application is meant to run as a Docker container and eventually will be optimized for deployment on k8s.

For now it's possible to run as a standalone container like so:

### Option 1: Build from source
```bash
# Grab source code
git clone https://github.com/clrosier/bills-api.git

# Build the docker image
docker build -t bills-api .

# Run the image as a container
docker run -d \
    --rm \
    --name bills-api \
    -p 5000:5000 \
    -e BILLS_API_DB_URL=ip_of_postgres_db \
    -e BILLS_API_DB_USER=my-user \
    -e BILLS_API_DB_PASS=my-admin-password \
    -e BILLS_API_DB_PORT=5432 \
    bills-api
```

### Option 2: Pull from Dockerhub
```bash
# Grab simage
docker pull clrosier/bills-api

# Run the image as a container
docker run -d \
    --rm \
    --name bills-api \
    -p 5000:5000 \
    -e BILLS_API_DB_URL=ip_of_postgres_db \
    -e BILLS_API_DB_USER=my-user \
    -e BILLS_API_DB_PASS=my-admin-password \
    -e BILLS_API_DB_PORT=5432 \
    bills-api
```
