# Healthcare Facilities

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

### Terraform Installation

This script automates the installation of Terraform on a Linux system. It downloads the Terraform binary, installs it, and sets up the environment.

To learn more about Terraform, visit the official documentation by clicking on this link: [Terraform Documentation](https://www.terraform.io/)

Instructions:

1. Navigate to the `bin` directory:

```bash
cd bin
```

2. Make the script executable:

```bash
chmod +x install_terraform.sh
```

3. Run the script:

```bash
./install_terraform.sh
```

4. Verify the installation:

```bash
terraform --version
```

5. Set tf alias, first make the script executable and then run it:

```bash
chmod +x set_tf_alias.sh \
./set_tf_alias.sh
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

To uninstall Terraform, run the following command to remove the binary:

```bash
sudo rm /usr/local/bin/terraform
```

Clean up any Terraform-related configuration files or state files if you no longer need them:

```bash
rm -rf ~/.terraform.d
rm -f .terraform.lock.hcl
```

**Note:** The above commands will remove the installations and all associated files from your system. Use with caution!
