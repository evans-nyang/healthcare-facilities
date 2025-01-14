# Healthcare Facilities

## Contents

- [Introduction](#introduction)
  - [Data Source and ETL Process](#data-source-and-etl-process)
  - [Data Summary](#data-summary)
- [Getting started](#getting-started)
- [Extras](#extras)

## Introduction

Our aim is to transform and integrate the data into a format that can be easily consumed by other systems. We'll use the Mage platform to author and share _healthcare_ data pipelines: creation of a pipeline that reads the data, transforms it, and writes it to a new location.

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

If you'd like to learn a bit more about Mage, check out the docs [here](https://docs.mage.ai/introduction/overview).

Data modeling and transformation will be done using **dbt**, a command-line tool that enables data analysts and engineers to transform data in their warehouse more effectively.

### Data Source and ETL Process  

The data sources for this project are the [Kenya Master Health Facility Registry](https://kmhfr.health.go.ke/public/facilities).

The ETL process is as follows:

1. Download the Kenya Master Health Facility List from the [Kenya Master Health Facility Registry](https://kmhfr.health.go.ke/public/facilities) website.

2. Extract the data from the Kenya Master Health Facility List api.

3. Transform the data by extracting the relevant columns and cleaning the data.

4. Load the data into postgres database.

### Data Summary

The attributes of the healthcare facilities dataset are as follows:

- `healthcare_facilities` table
  - `code` (integer): Unique identifier for the healthcare facility.
  - `name` (string): Name of the healthcare facility.
  - `registration number` (string): Registration number of the healthcare facility.
  - `keph level` (string): Level of the healthcare facility.
  - `facility type` (string): Type of the healthcare facility.
  - `owner` (string): Owner of the healthcare facility.
  - `regulatory body` (string): Regulatory body of the healthcare facility.
  - `bed` (integer): Bed capacity of the healthcare facility.
  - `cots` (integer): Cots capacity of the healthcare facility.
  - `county` (string): County where the healthcare facility is located.
  - `constituency` (string): Constituency where the healthcare facility is located.
  - `sub_county` (string): Sub-county where the healthcare facility is located.
  - `ward` (string): Ward where the healthcare facility is located.
  - `operation status` (string): Operation status of the healthcare facility.
  - `open_whole_day` (string): Whether the healthcare facility is open the whole day.
  - `open_public_holidays` (string): Operational status during public holidays.
  - `open_weekends` (string): Operational status during weekends.
  - `open_late_night` (string): Whether the healthcare facility is open late at night.
  - `service names` (string): Names of the services offered by the healthcare facility.
  - `approved` (string): Approval status of the facility.
  - `public_visible` (string): Public visibility status of the facility.
  - `closed` (string): Whether the healthcare facility is closed.

## Getting started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/).

Navigate to the directory:

```bash
cd healthcare-facilities/mage
```

Rename `.env_example_mage` to simply `.env`— this will ensure the file is not committed to Git by accident, since it contains the credentials. Change the values in the `.env` file to match your environment.

```bash
mv .env_example_mage .env
```

Now, build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to <http://localhost:6789> in your browser! 🚀

### Extras

We just initialized a new mage repository. It will be present in your project under the name `mage`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

The resources in the links below might come in handy:

1. [Mage Docs](https://docs.mage.ai/introduction/overview): understand Mage functionality or concepts.
2. [Dbt Docs](https://docs.getdbt.com/docs/introduction): grasp comprehension of dbt functionality or concepts.
