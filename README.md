# Healthcare Facilities in Kenya

## Table of Contents

- [Problem Description](#problem-description)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [License](#license)
- [Contributing](#contributing)

## Problem Description

Healthcare facilities are a critical component of any healthcare system. They provide the necessary infrastructure for the delivery of healthcare services. However, the availability of healthcare facilities is not uniform across different regions, some regions have a higher concentration compared to others. This disparity in the distribution can have a significant impact on the health outcomes of the population. We'll explore the distribution of healthcare facilities in Kenya and identify regions that are underserved in terms of healthcare facilities.

The project is intended to be a resource for researchers, policymakers, and other stakeholders interested in understanding the distribution and availability of healthcare facilities in Kenya. It provides a comprehensive dataset of healthcare facilities in the country and a set of tools for exploring and analyzing the data.

## Project Structure

The project is divided into four main components:

- Environment Setup : This document provides information on setting up the environment for the project.

- ETL : Extract-Transform-Load process, the data models and analyses for exploring the data.

- Visualization : Data visualization platform for exploring the healthcare facilities data.

- Healthcare Assistant : This documentation comprises the language model for the healthcare assistant application.

The project tree directory structure is as follows:

```md
healthcare-facilities
├── bin
│   ├── install_docker.sh
│   ├── install_miniconda.sh
│   └── README.md
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
│   │   ├── rag.py
│   │   └── streamlit_app.py
│   ├── notebooks
│   │   ├── evaluation_data_generation.ipynb
│   │   └── health_rag_flow.ipynb
│   ├── tests
│   │   └── test.py
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── env_example_llm
│   ├── README.md
│   ├── requirements.txt
│   └── test.py
│
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
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
└── requirements.txt
```

## Documentation

Check out the documentation for each component below:

- [Environment Setup](bin/README.md)
- [Data Sources and ETL Process](mage/README.md)
- [Data Visualization](visualization/superset/README.md)
- [Healthcare Assistant](healthcare_assistant/README.md)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.
