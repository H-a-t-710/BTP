# Flask Application with Database Migrations

## Overview

This project is a Flask web application that uses SQLAlchemy for ORM and Flask-Migrate for handling database migrations. The application includes user authentication, data storage, and a dashboard feature.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-Migrate

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
2. **Create a Virtual Environment**
   ```bash
   python -m venv venv

3. **Activate the Virtual Environment**
  - Windows
    ```bash
    venv\Scripts\activate
  - macOs/Linux
    ```bash 
    source venv/bin/activate
4. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

# Configuration
  ## Set Up the Flask Application
  Ensure your Flask app is configured correctly. For development purposes, you can set the SECRET_KEY and database URI directly in your app.py or config.py.
# Database Migrations
   Flask-Migrate is used to handle database schema changes. Follow these steps to initialize and manage your database:
  1. **Initialize the Migration Repository**
       This creates the migrations folder which will contain the migration scripts.
      ```bash
     flask db init
  2. **Create a Migration Script**
      This command auto-generates a migration script based on changes detected in your models.
      ```bash
     flask db migrate -m "Initial Migration"
  3. **Apply the Migrationt**
    This updates the database schema based on the migration script.
      ```bash
      flask db upgrade
 4. **Apply the Migrationt**
   This rolls back the database schema to the previous version.
      ```bash
      flask db downgrade
# Running the Application
  To start the Flask application, use:
  ```bash
    flask run




   


