# Healthcare facilities in Kenya

Healthcare facilities data in Kenya

## Table of Contents

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
├── superset
│   ├── .env_superset_example
│   ├── Dockerfile
│   ├── docker-compose-superset.yml
│   ├── superset_config.py
│   ├── superset_init.sh
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

- [Data Sources and ETL Process](mage/README.md)
- [Data Visualization](superset/README.md)

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please see the [Contributing Guidelines](CONTRIBUTING.md) for more details.
