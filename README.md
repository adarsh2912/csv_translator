# csv_translator

## Problem statement
1.An API which enables users to upload the farmer list via a csv file and translates the
data into supported languages(in this case supported languages are: Hindi, Marathi, Telugu and Punjabi). Sample list can be found in **tmp** folder above.<br/>
2. An API which allows us to retrieve all farmer data in the subset of languages specified
above.

## Assumptions for the above problem statements
1. At a time multiple user can request for translating the csv file.
2. CSV file can contains thousands of rows.

## Approach for the solution 
1. As their are multiple request are being made at a single time with huge amount of data to be translated in multiple supporting languages and we are relying on external API calls to translate huge amount of data it can takes some time to translate the data that why i decided to make **non-blocking** POST request for translating CSV data.
2. POST request for traslating CSV data will Take csv file with request and returns the status-code 202(Accepted) with response body something like:<br/>
`{
    "msg": "uploaded successfully",
    "file_id": "6346d9719e1a731be2728066",
    "job_id": "2e5e9a62-40fc-41f3-8e65-550e7489549f"
}`
3. In Background data will get translated using **Google Translate API** and saved in Database.
4. Any time we can check our background translation Job Status by GET request using **Job_id** that we have got in above response.
5. After the Job is done we can fetch our translated data from a GET request with **file_id**. 

## Project Setup Guide:

### Prerequisites
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
