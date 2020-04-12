# ---- Base python ----
FROM python:3.6 AS base
# Create app directory
WORKDIR /bills-api

# ---- Dependencies ----
FROM base AS dependencies
COPY requirements.txt ./
# install app dependencies
RUN pip install -r requirements.txt

# ---- Copy Files/Build ----
FROM dependencies AS build
WORKDIR /bills-api
COPY . /bills-api
# Build / Compile if required

# --- Release with Alpine ----
FROM python:3.6-alpine3.7 AS release
# Create app directory
WORKDIR /bills-api

COPY --from=dependencies /bills-api/requirements.txt ./
COPY --from=dependencies /root/.cache /root/.cache

# Install app dependencies
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc libffi-dev musl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk del gcc libffi-dev musl-dev

COPY --from=build /bills-api/ ./
CMD ["gunicorn", "--config", "gunicorn_conf.py", "manage:app"]
