# Healthcare Facilities

## Visualizing data with Apache Superset

Apache Superset is a modern, enterprise-ready business intelligence web application. It's a fast, lightweight, and intuitive way to visualize data and build dashboards. Superset allows you to create, organize, and share data in a secure environment.

The goal of this project is to demonstrate how to use Apache Superset to visualize data. We'll be working with a dataset of healthcare facilities in Kenya. The dataset contains information about the facilities, such as the facility name, type, county, and location.

If you'd like to learn a bit more about Apache Superset, check out the docs [here](https://superset.apache.org/).

## Getting started

This repo contains a Docker Compose template for getting started with a new Apache Superset project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/).

Navigate to the directory:

```bash
cd healthcare-facilities/superset
```

Rename `.env_example_superset` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it contains the credentials. Change the values in the `.env` file to match your environment.

Now, build the container

```bash

docker compose build
```

Finally, start the Docker container:

```bash
docker compose -f docker-compose-superset.yml up
```

Now, navigate to <http://localhost:8088> in your browser!
