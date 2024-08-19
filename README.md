# Homelab
Hi my name is Will. Welcome to my HomeLab repository! This repository contains a collection of helpful configuration files, focusing on Docker and Ansible setups, to streamline the management and automation of my personal home lab environment. This repository is intended for my own use, but feel free to explore and use any configurations that might benefit your own setup.

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Requirements](#requirements)
* [Contributing](#contributing)
* [License](#license)

## Introduction
This repository is a central place for all the configuration files I use in my home lab. It includes Docker configurations for containerized applications and Ansible playbooks for automated setups and maintenance tasks. Be aware these configuration files are subject to change and directories may expand in future should I find better implementations.

> :warning: Be aware, software files can change over time. I do my best to keep up with the latest changes and releases, but please understand that this won’t always be the case.

## Features
* **Unifi**: I use their hardware for switches and routing at the moment...below is a link for the officially supported unifi controller service install script for Linux.

    * <a href="https://glennr.nl/s/unifi-network-controller" target="_blank" rel="noopener noreferrer">Glenn R. Unifi Install Script</a>
* **Docker Configurations**: mostly docker compose files for docker containers that host various foundational services in a network

    * <a href="https://docs.docker.com/" target="_blank" rel="noopener noreferrer">Docker Documentation</a>

* **Ansible Playbooks**: used to automate server configurations and deployments (this is still in an very early state in the repo)

    * <a href="https://docs.ansible.com/" target="_blank" rel="noopener noreferrer">Ansible Documentation</a>
    * <a href="https://github.com/semaphoreui/semaphore" target="_blank" rel="noopener noreferrer">Ansible Sempahore (Open-Source Ansible UI)</a>
* **Documentation** Notes and guides to help understand and use the configurations properly

## Requirements
1. Use a virtualization platform (such as Proxmox) to run VMs so we can make good use out of Ansible, specifically Ansible playbooks - below are some common virtualization platforms
* **Proxmox** <a href="https://www.proxmox.com/en/proxmox-virtual-environment/get-started" target="_blank" rel="noopener noreferrer">Install</a> - This is what I use
* **XCP-ng** <a href="https://docs.xcp-ng.org/installation/install-xcp-ng/" target="_blank" rel="noopener noreferrer">Install</a>
* **VMware** <a href="https://www.vmware.com/tryvmware_tpl/hypervisor7.html" target="_blank" rel="noopener noreferrer">Install</a>  - NOTE: Requires licensing

2. Highly recommended you use a Linux OS distribution for running docker

3. Have some basic knowledge of networking, containers, and an idea of [IAC](https://aws.amazon.com/what-is/iac/#:~:text=Infrastructure%20as%20code%20(IaC)%20is,%2C%20database%20connections%2C%20and%20storage.) (infrastructure as code)

## Contributing
This repository is primarily for personal use, but if you have suggestions or improvements, feel free to submit a pull request. Ensure that your contributions align with the goals of the repository and adhere to good coding standards.

1. **Fork** the repository.

2.  Create a new **branch** (```git checkout -b feature-branch```).

3. Make your **changes**.
4. Commit your changes (```git commit -m 'Add new feature'```)
5. **Push** to the branch (```git push origin feature-branch```).
6. Open a **pull request**.

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/willb6879/homelab/blob/main/LICENSE) file for details.


---

Thank you for checking out my HomeLab repository! If you have any questions or need further assistance, feel free to open an issue. Happy configuring!
