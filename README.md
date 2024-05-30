# Homelab
Hi my name is Will. Welcome to my HomeLab repository! This repository contains a collection of helpful configuration files, focusing on Docker and Ansible setups, to streamline the management and automation of my personal home lab environment. This repository is intended for my own use, but feel free to explore and use any configurations that might benefit your own setup.

## Table of Contents
* Introduction
* Features
* Requirements
* Installation
* Usage
* Contributing
* License

## Introduction
This repository is a central place for all the configuration files I use in my home lab. It includes Docker configurations for containerized applications and Ansible playbooks for automated setups and maintenance tasks. Be aware these configuration files are subject to change and directories may expand in future should I find better implementations.

## Features
* **Docker Configurations**: mostly docker compose files for docker containers that host various foundational services in a network
* **Ansible Playbooks** scripts to automate server configurations and deployments (this is still in an early state in the repo)
* **Documentation** Notes and guides to help understand and use the configurations properly

## Requirements
* It is recommended that you have some sort of virtualization node(s) although a single local host will work as well. We want a virtualization node (such as Proxmox) so we can make good use out of Ansible, specifically Ansible playbooks
* **Highly recommended** you use a linux OS distrobution for running docker
* Some basic knowledge of networking, Docker and Ansible

## Installation
1. Clone the repo
```bash
git clone https://github.com/yourusername/homelab.git # https
git clone git@github.com:yourusername/homelab.git # ssh
gh repo clone willb6879/homelab # github CLI
```
