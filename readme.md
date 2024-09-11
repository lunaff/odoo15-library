# Odoo 17 for DKH

This is project for odooo 17 in dkh

## Preparation

For install this project make sure you have
- Linux(Debian, Ubuntu, etc)
- Docker
- Portainer

## Installation

- Install Docker
[Docker](https://docs.docker.com/engine/install/)

- Install Portainer
[Portainer](https://docs.portainer.io/start/install-ce/server/docker/linux)

- Clone this repository
```bash
    git clone https://github.com/sholludev/erp-dkh.git
    cd erp-dkh
```

- Copy `docker-compose.yml.bak` into `docker-compose.yml`

- Build odoo in docker by this command
```bash
    sudo docker compose up -d
```

## Check

For check your installation successfully or not just open you browser than type `localhost:8019`


