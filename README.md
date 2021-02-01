# Inventory Website for TMLEnergy

The website is developed using Django Web Framework. It is used for managing inventory items on TMLEnergy.

Currently supports items entry based on category only.

Planned features:
1. Inventory list view.
2. Search items based on item's name.
3. Sort view based on columns.
4. List items with only specified features.
5. Edit items.
6. Delete items.


## Requirements:
1. Windows 8/8.1 above (Windows 7 or older can only use Django version 2), Linux, or Mac OS X
2. Python with minimum version of 3.8.6
3. Virtualenv module
4. .env file of this project (ask me on email!)
5. Your chosen IDE configured for developing Django Apps

## Local Deployment Steps
1. Install Python (if not yet installed) and pip (Python Package Manager). Then install virtualenv using:
   
   `pip install virtualenv`.

2. Create new isolated environment for project using on a new folder this command:

    `virtualenv venv`

3. Clone this repository using:
   
   `git clone https://github.com/gnumi34/inventory-website.git`

4. Install the requirements:

    `pip install -r requirements.txt`

5. Run migrations to create DB file:

    `python3 manage.py makemigrations`

    `python3 manage.py migrate`

6. Run the apps:
   
   `python3 manage.py runserver`

   and open the apps on `localhost:8000`