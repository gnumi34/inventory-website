# Inventory Website for TMLEnergy

The website is developed using Django Web Framework. It is used for managing inventory items on TMLEnergy.

Currently supports items entry based on category only.

Planned features:

1. Update search form choices every item entry.
2. Sort view based on columns.
3. Stricter user authentication and permissions.
4. Add email backend for password reset feature.

## Requirements

1. Windows 8/8.1 above (Windows 7 or older can only use Django version 2), Linux, or Mac OS X
2. Python with minimum version of 3.8.6
3. Virtualenv module
4. Memcached installed
5. .env file of this project (ask me on email!)
6. Your chosen IDE configured for developing Django Apps

## Local Deployment Steps

1. Install Python, pip (Python Package Manager), virtualenv, and memcached if you have not installed them.

2. Open your OS's terminal. Start memcached with this command:

    `memcached -p 11211`

    Don't close the terminal window!

3. Clone this repository using:

   `git clone https://github.com/gnumi34/inventory-website.git`

4. Create new isolated environment for project inside inventory-website folder using:

    `virtualenv venv`

5. On Linux, activate the isolated environment using:

    `source venv/bin/activate`

    While on Windows, activate the isolated environment based on your terminal.

    For Command Prompt: `venv\Scripts\activate.bat`

    For PowerShell: `venv\Scripts\activate.ps1`

    Make sure the terminal is shown like this:

    `(venv) user@laptop:/home/user/inventory-website/`

6. Install the requirements:

    `pip install -r requirements.txt`

7. Run migrations to create DB file:

    `python3 manage.py makemigrations data_entry`

    `python3 manage.py migrate`

8. Run the apps:

   `python3 manage.py runserver`

   and open the apps on `localhost:8000`
