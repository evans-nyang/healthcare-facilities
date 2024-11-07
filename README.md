# Healthcare Facilities in Kenya

## Table of Contents

- [Problem Description](#problem-description)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [License](#license)
- [Contributing](#contributing)

## Problem Description

Healthcare facilities are a critical component of any healthcare system. They provide the necessary infrastructure for the delivery of healthcare services. However, the availability of healthcare facilities is not uniform across different regions, some regions have a higher concentration compared to others. This disparity in the distribution can have a significant impact on the health outcomes of the population. In this project, we will explore the distribution of healthcare facilities in Kenya and identify regions that are underserved in terms of healthcare facilities.

The goal of this project is to create a tool that will help users find healthcare facilities information in different regions of Kenya. The tool will provide information on the number of healthcare facilities in a given region, the type of facilities available, their location and other related information. This will help users to identify regions that are underserved and in need of additional resources.

The project is intended to be a resource for researchers, policymakers, and other stakeholders interested in understanding the distribution and availability of healthcare facilities in Kenya. It provides a comprehensive dataset of healthcare facilities in the country and a set of tools for exploring and analyzing the data.

## Project Structure

The project is divided into four main components:

1. [**Environment Setup**](bin/README.md): This document provides information on setting up the environment for the project. It includes instructions for installing the necessary tools, libraries and configuration files. The directory also includes installation scripts and files for setting up the project environment.

2. [**ETL**](mage/README.md): This comprises the data sources and collection process for obtaining the healthcare facilities data. It provides information on the data sources used, the data collection process, and the data schema for the dataset; including ETL process for extracting, transforming, and loading the healthcare facilities data into a database. It also includes the data models and analyses for exploring the data.

3. [**Visualization**](visualization/superset/README.md): This document includes the data visualization platform for exploring the healthcare facilities data. It uses Apache Superset as the visualization tool and provides a set of dashboards and visualizations for analyzing the data.

4. [**Healthcare Assistant**](healthcare_assistant/README.md): This documentation comprises the language model for generating healthcare-related questions and answers. It contains information on the language model used, the data sources, and the training process for the model. It also includes the code for generating questions and answers using the language model. The directory also includes the notebooks for training the language model and generating the questions and answers.

The tree directory structure is as follows:

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
├── healthcare_assistant
│   ├── data
│   │   ├── ground_truth_retrieval.csv
│   │   ├── kenya_health_facilities_clean.csv
│   │   └── kenya_health_facilities.csv
│   ├── grafana
│   │   ├── dashboard.json
│   │   ├── grafana_queries.md
│   │   └── init.py
│   ├── healthcare_assistant_app
│   │   ├── app.py
│   │   ├── db_prep.py
│   │   ├── db.py
│   │   ├── ingest.py
│   │   ├── minsearch.py
│   │   ├── models.py
│   │   └── rag.py
│   ├── notebooks
│   │   ├── evaluation_data_generation.ipynb
│   │   ├── health_rag_flow.ipynb
│   │   └── minsearch.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── env_example_llm
│   ├── README.md
│   ├── requirements.txt
│   ├── streamlit_app.py
│   └── test.py
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
- [Healthcare Assistant](healthcare_assistant/README.md)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.
