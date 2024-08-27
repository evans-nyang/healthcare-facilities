# Healthcare Facilities Language Model

## Contents

- [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [Miniconda Installation](#miniconda-installation)
  - [Docker Installation](#docker-installation)
- [Extras](#extras)

## Usage

### Prerequisites

- A Linux-based operating system
- `wget` installed on your system

### Miniconda Installation

This script automates the installation of Miniconda on a Linux system. It downloads the Miniconda installer, installs it, and sets up the environment.

To learn more about Miniconda, visit the official documentation by clicking on this link: [Miniconda Documentation](https://docs.anaconda.com/miniconda/)

Instructions:

1. Navigate to the `bin` directory:

```bash
cd bin
```

2. Make the script executable:

```bash
chmod +x install_miniconda.sh
```

3. Run the script:

```bash
./install_miniconda.sh
```

### Docker installation

This script automates the installation of Docker on a Linux system. It downloads and installs the latest version of Docker engine and Docker Compose, adds the current user to the `docker` group, and sets up the environment.

To learn more about Docker, visit the official documentation by clicking on this link: [Docker Documentation](https://docs.docker.com/)

Instructions:

1. Navigate to the `bin` directory:

```bash
cd bin
```

2. Make the script executable:

```bash
chmod +x install_docker.sh
```

3. Run the script:

```bash
./install_docker.sh
```

## Extras

To uninstall Miniconda, run the following command:

```bash
rm -rf ~/miniconda
```

To uninstall Docker, run the following commands:

```bash
sudo apt-get purge docker-ce docker-ce-cli containerd.io
sudo rm -rf /var/lib/docker
sudo groupdel docker
```

Note: The above commands will remove Docker and all its associated files from your system. Use with caution.
