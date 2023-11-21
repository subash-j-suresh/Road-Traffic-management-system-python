## Prerequisites
- Install python >=3.9 <=3.12
- Install poetry

## Setting up the project
1. Run the below command to install dependencies
    ```
    poetry install --no-root
    ```
    this should create the following files in the project
    - a `.venv` folder in the project folder.
    - `poetry.lock` file. Do not edit this!!!
2. To start the virtual environment run
    ```
    poetry shell
    ```
    this should activate the virtual environment.

once these steps are performed you are all set to run the project.

# Database Operations Console Application

This console application allows users to perform various database operations using a console-based interface. The application utilizes Python and MySQL to interact with the database.

## Overview

This repository contains a console-based application that facilitates a range of database operations, from basic CRUD functionalities to more advanced SQL operations.

## Features

- **CRUD Operations:** Create, Read, Update, and Delete records from the database.
- **Advanced SQL Operations:**
  - **Set Operations:** Union, Intersection, and Difference of tables.
  - **Set Membership Checks:** IN Membership, EXISTS Membership.
  - **Set Comparisons:** Less Than, Greater Than, Equal To comparisons between tables.
  - **Subqueries with WITH Clause:** Advanced subquery functionalities.
  - **Advanced Aggregate Functions:** Aggregate functions beyond the basics.

## Setup

### Requirements

- Python 3.x
- MySQL database
- `mysql-connector-python` library (`pip install mysql-connector-python`)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/database-console-app.git