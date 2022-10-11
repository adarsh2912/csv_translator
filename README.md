# csv_translator

## Prerequisites
--> Keep running mongodb on localhost<br/>
--> Run RabbitMQ messaging-broker [installation guide](https://www.rabbitmq.com/#getstarted)

### Step 1 - Clone project
`git clone https://github.com/adarsh2912/csv_translator.git`

### Step 2 - Create python virtual envirnonment.
`cd csv_translator` <br/>
`python -m venv env`

### Step 3 - Activate virtual environment.
Linux <br/>
`source env/bin/activate`<br/>
Windows<br/>
`env/Scripts/Activate.ps1`

### Step 4 - Install dependencies from requirements.txt.
`pip install -r requirements.txt`

### Step 5 - Run migrations
`python manage.py migrate`

### Step 6 - Add .env file in project directory and add the google API-KEY with below named.
`GOOGLE_APPLICATION_CREDENTIALS='<your-api-key>'`

### Step 7 - Run Django application server on terminal.
`python manage.py runserver`

### Step 8 - Open new terminal and run celery worker.
linux<br/>
`celery -A csvtranslator worker --loglevel=INFO`<br/>
windows<br/>
`celery -A csvtranslator worker -l info -P gevent`

If everything is running well you can import the api document from project folder name **csv_translator_API_DOC.postman_collection.json**
and sample csv file from **tmp** folder to test the APIs.
