# Healthcare Facilities

## Mage AI

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

We'll use the Mage platform to author and share _healthcare_ data pipelines.
If you'd like to learn a bit more about Mage, check out the docs [here](https://docs.mage.ai/introduction/overview).

## Getting started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/).

You can start by cloning the repo:

```bash
git clone https://github.com/evans-nyang/healthcare-facilities.git
```

Navigate to the directory:

```bash
cd healthcare-facilities/mage
```

Rename `.env_example_mage` to simply `.env`— this will _ensure_ the file is not committed to Git by accident, since it contains the credentials. Change the values in the `.env` file to match your environment.

Now, build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to <http://localhost:6789> in your browser! 🚀

### What just happened?

We just initialized a new mage repository. It will be present in your project under the name `mage`. If you changed the varable `PROJECT_NAME` in the `.env` file, it will be named whatever you set it to.

This repository should have the following structure:

```
.
├── healthcare
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── .env
├── docker-compose.yml
└── requirements.txt
```

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
