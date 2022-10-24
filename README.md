# Simple Web App + Web Service

This project contains two applications:
- A simple web application with VueJS Framework.
- A simple web service for providing REST API, built on top of the Django REST Framework.

## Prerequisite

### Docker

All applications run in Docker containers. Local orchestration is handled by _docker-compose_. That being said, to install Docker on your machine, you can follow the steps in the particular links found below:

For machines running **MacOS** you can follow steps explained [here](https://docs.docker.com/docker-for-mac/install/)

For machines running **Linux (Ubuntu)** you can follow steps explained [here](https://docs.docker.com/desktop/install/linux-install/)

Please note that _docker-compose_ is also needed to be installed so we're able to start the project the way it should be.

### How to Start the Project

```
$ docker-compose up --build
```

### How to stop the Project

```
$ docker-compose down --remove-orphans
```
