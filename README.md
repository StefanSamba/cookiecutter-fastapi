# Cookiecutter API Templating

Article: [TBD]()
<video src='cookiecutter-fastapi.mov'></video>

## Description

- Don't know how to get started with building APIs?
- Tired of copy pasting folders when creating a new API?

Use this cookiecutter-fastapi repo to generate your API. The goal of this repo is to speed up your api development. The goal is not to provide you with a full functioning tailored API.

Use this repo to generate a base for your API. Next, tailor it to you specific use case.

## Features

- Option for local development in a virtual environment
- Option to run the service as a container with a Dockerfile as well as Docker Compose
- 1 API folder where different subfolders can be added for different endpoint versions (e.g. v1/)
- 1 schema folder for input validation
- 1 utils folder where custom functions can be added
- 1 model folder where a predictive model can be added
- 1 default GET endpoint
- 1 GET endpoint that can be used for a health check
- 1 POST endpoint
- 1 tests folder that includes pytest examples integrated for these 3 endpoints

## Pre-requisites

1. Install cookiecutter

```bash
pip3 install cookiecutter
```

## Usage

1. Open the terminal and navigate to the folder where you'd like to create your API.

2. Generate your API

```bash
cookiecutter https://github.com/StefanSamba/cookiecutter-fastapi.git
```

3. Enter details in CLI
   The CLI will ask for a project name and endpoint name. Only letters and underscores are allowed here.

For example:
project name: sample_project
endpoint name: analyze_text

Done, your project is ready for use. See readme in your project for more details on how to run it.

## Contributing

This project is open to contributions.
