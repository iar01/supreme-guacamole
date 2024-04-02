## Project Title

*Provide a brief description of your Django REST API Project*

### Table of Contents

* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Application](#running-the-application)
* [Usage](#usage)

### Getting Started

1. **Clone the Repository**

   ```bash
   git clone [https://github.com/iar01/supreme-guacamole](https://github.com/iar01/supreme-guacamole)
    ```
## Prerequisites

Before getting started, please ensure you have the following:

* **Python 3.6 or later:** Download the latest version from https://www.python.org/downloads/
* **pip (package installer for Python):** Instructions to install pip can be found at https://pip.pypa.io/en/stable/installation/
* **A code editor or IDE:**
    * Visual Studio Code: https://code.visualstudio.com/
    * PyCharm: https://www.jetbrains.com/pycharm/
* **(Optional) Git for version control:** https://git-scm.com/ 


## Setup

Follow these steps to set up your development environment:

**1. Create a Virtual Environment**

   It's highly recommended to work within a virtual environment to manage your project's dependencies effectively.

   * **Windows:**
     ```bash
     python -m venv env
     env\Scripts\activate.bat 
     ```

   * **macOS/Linux:**
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

**2. Install Dependencies**

   The `requirements.txt` file contains all the necessary Python packages for your project. Install them using pip:

   ```bash
   pip install -r requirements.txt
   ```
## Running the Application

To start your Django REST API locally:

1. **Apply Migrations**

   Make sure your database is up-to-date with your project's models:

   ```bash
   python manage.py makemigrations
   ```
   
   ```bash
   python manage.py migrate
   ```
  
2. **Collect Static**

    Before deploying your application, it's essential to collect all static files into a central location:

     ```bash
   python manage.py collectstatic
   ```
   
3. **Create a Superuser**

    To manage your Django project through the admin interface, you'll need to create a superuser account:

     ```bash
   python manage.py createsuperuser
   ```

4. **Runserver**

    To start the development server and begin testing your API:

     ```bash
   python manage.py createsuperuser
   ```

   