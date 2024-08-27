# Healthcare facilities in Kenya

Healthcare facilities data in Kenya

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
- [Documentation](#documentation)
- [License](#license)
- [Contributing](#contributing)

## About the Project

This project aims to provide a comprehensive dataset of healthcare facilities in Kenya. The dataset includes information on the location, type, and services offered by healthcare facilities in Kenya. The project also includes a data pipeline for extracting, transforming, and loading the data into a database, as well as a data visualization platform for exploring the data.

The project is divided into three main components:

1. [**Environment Setup**](bin/README.md): This document provides information on setting up the environment for the project. It includes instructions for installing the necessary tools, libraries and configuration files. The directory also includes installation scripts and files for setting up the project environment.

2. [**ETL**](mage/README.md): This comprises the data sources and collection process for obtaining the healthcare facilities data. It provides information on the data sources used, the data collection process, and the data schema for the dataset; including ETL process for extracting, transforming, and loading the healthcare facilities data into a database. It also includes the data models and analyses for exploring the data.

3. [**Visualization**](visualization/superset/README.md): This document includes the data visualization platform for exploring the healthcare facilities data. It uses Apache Superset as the visualization tool and provides a set of dashboards and visualizations for analyzing the data.

4. [**Language Model**](llm_health/README.md): This documentation comprises the language model for generating data for the faq section for the healthcare facilities dataset. It uses multiple language models to generate questions and answers for the faq section.

The project is intended to be a resource for researchers, policymakers, and other stakeholders interested in understanding the distribution and availability of healthcare facilities in Kenya. It provides a comprehensive dataset of healthcare facilities in the country and a set of tools for exploring and analyzing the data.

## Getting Started

### Prerequisites

- Python (version >= 3.8)
- Docker (version >= 20.10)
- Docker Compose (version >= 1.29)

### Project Structure

The project structure is as follows:

```md
healthcare-facilities
├── mage
│   ├── healthcare
│   │   ├── charts
│   │   ├── custom
│   │   ├── data_exporters
│   │   ├── data_loaders
│   │   ├── dbt/health_base
│   │   │   ├── analyses
│   │   │   ├── macros
│   │   │   ├── models
│   │   │   ├── tests
│   │   │   ├── .env_example_dbt
│   │   │   ├── dbt_project.yml
│   │   │   ├── packages.yml
│   │   │   └── profiles.yml
│   │   ├── extensions
│   │   ├── interactions
│   │   ├── pipelines
│   │   ├── scratchpads
│   │   ├── transformers
│   │   ├── utils
│   │   ├── __init__.py
│   │   ├── io_config.yaml
│   │   └── metadata.yaml
│   ├── .env_example_mage
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
│
├── visualization
│   └── superset
│       ├── .env_superset_example
│       ├── Dockerfile
│       ├── docker-compose-superset.yml
│       ├── superset_config.py
│       ├── superset_init.sh
│       ├── superset_init.sh
│       └── README.md
│
├── llm_health
│   ├── .env_example_llm
│   ├── index_data.py
│   ├── ground_truth_health_data.ipynb
│   ├── generate_faq_data.py
│   ├── docker-compose-llm.yml
│   └── README.md
│
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Documentation

The documentation for this project is as follows:

- [Environment Setup](bin/README.md)
- [Data Sources and ETL Process](mage/README.md)
- [Data Visualization](visualization/superset/README.md)
- [Language Model](llm_health/README.md)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.
