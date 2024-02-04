# Price Quote Tracker

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Integration Tests](#integration-tests)
- [Design Questions](#design-questions)
- [License](#license)

## Overview

A Simple REST API that tracks different Providers price quotes for different Artifacts, built as a solution to the infoStrategy asssessment

## Prerequisites

You need to have Python3.xx installed in order to run this application.

## Installation

```bash
# Clone the repository
git clone https://github.com/coderboy-exe/info-strat.git

# Navigate to the project directory
cd info-strat

# Create a virtual environment (my_env)
python -m venv my-env

# Activate your virtual environment
# Windows (Assuming you are using a bash terminal)
source my-env/Scripts/activate
# Linux
source my-env/bin/activate 

# Install dependencies
pip install -r requirements.txt

# Perform any additional setup steps (database migrations, etc.)
python manage.py migrate

```

## Usage

Simply run the dev server

```bash
# Run the development server
python manage.py runserver
```

Access the application at [http://localhost:8000](http://localhost:8000).


## API Documentation

Check out the comprehensive [Postman documentation](https://documenter.getpostman.com/view/27182139/2s9YyvCLSQ)

## Integration Tests

Run the **"Integration Tests"** folder in the [Postman collection](https://documenter.getpostman.com/view/27182139/2s9YyvCLSQ)

All tests should pass


Refer to the [API documentation](https://documenter.getpostman.com/view/27182139/2s9YyvCLSQ) for detailed information as well as examples for each endpoint.

## Design Questions

Solution to the theoretical design questions can be found in the [**Answers.md**](Answers.md) file


## License

This project is free for distribution under the [MIT License](#license).
