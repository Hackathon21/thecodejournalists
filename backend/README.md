# Backend + REST API for *Verify* NEWS

The backend is built with Django, Django Rest Framework, and ML and DS libraries like pandas, numpy, and scikit-learn. The database stores the news scraped from different sources and user data liked saved articles and their votes. Cleaned data is also stored in the Django SQLite database. Stored data and ML results are being exposed by the api so that our React frontend can access the data.

<br>

> **NOTE:** Using SQLite instead of PostgreSQL so that the DB can directly be pushed into production.

<br>

## Technologies Used:
- Django
- Django Rest Framework
- DS and ML libraries like numpy, pandas and scikit-learn
- Sqlite3 Databases
- Possibly, Docker

<br>

## TRY IT OUT:

First, navigate to the root of the project repo. 

Now generate the static files using the following npm command:
```
# This will install all npm dependencies in the node_modules/ folder
npm i           

# To generate the static files
npm run dev
```
This will create a new file called `webpack-stats.json` in the root folder. 

The next step is to create a new virtual environment for our Python Django project. We will also activate it and install all the dependencies.
```
# Upgrade pip for latest updates
python -m pip install --upgrade pip     

# Name your virtual environment anything - like '.venv'
python -m venv .venv     

# Activate the virtual environment
.venv/Scripts/activate (Windows) 
.venv/bin/activate (Linux)

# Update pip inside the activated environment
python -m pip install --upgrade pip  

# Install the requirements
pip install -r requirements.txt
``` 

Then, launch the Django project using:
```
python manage.py runserver
```
This will start a server on a local address [http://127.0.0.1:8000](http://127.0.0.1:8000)


## All this to run a Web App?
Whoa, that was a lot of steps for starting a single web app. It's because of the need for a Django Python backend and Analysis through ML.
Having different technologies in a single project requires not just their own configuration/dependency installation but also a need to configure them to work together.

<br><br>

# CONTRIBUTING:

To contribute to this project, you need to repeat all the steps performed above, except that you need to replace the command `npm run dev` with `npm run watch`. Unlike `dev`, the `watch` command will generate static files every time you edit your source, which is required when developing your web app.

## Guidelines:
- Do not mess with the `frontend/` folder
- Make sure to run `python manage.py makemigrations` before `python manage.py migrate`
- Also, check if the code is correct using `python manage.py check` before `python manage.py runserver`
- Python changes are hot reloaded, so only reload the page after making changes in a static file.
- Make sure to include webpack provided CSS and JS files instead of loading them with the static tag.
- Do not mess with SQL migration files unless you know what you're doing
- All the project apps are stored under the `backend/apps/` folder.
- The API is accessible through the `api/` route.
- The Admin is accessible through the `watch-tower` route instead of `admin` (for better security)
- Try to write tests for testing all Django functionalities.
  

## Admin Login Credentials
- **Username:** batman
- **Password:** enter$b@tc@ve

<br>

## ***Now, just go and build stuff!*** 