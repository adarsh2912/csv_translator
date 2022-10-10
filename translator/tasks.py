import os
import json
import environ
import requests
from celery import shared_task
from pathlib import Path
from translator.models import Translations
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
env = environ.Env()
environ.Env.read_env(os.path.join(Path(__file__).resolve().parent.parent, '.env'))

@shared_task(serializer='json')
def translate_csv_data(fieldName, rows_data, fileId):
  hindi_trans = google_translator_function(rows_data, target_language='hi')
  marathi_trans = google_translator_function(rows_data, target_language='mr')
  telugu_trans = google_translator_function(rows_data, target_language='te')
  punjabi_trans = google_translator_function(rows_data, target_language='pa')
  english = [rows_data[item:item + 5] for item in range(0, len(rows_data), 5)]
  for item in range(4):
    en = dict(zip(fieldName, english[item]))
    hi = dict(zip(fieldName, hindi_trans[item]))
    mr = dict(zip(fieldName, marathi_trans[item]))
    te = dict(zip(fieldName, telugu_trans[item]))
    pa = dict(zip(fieldName, punjabi_trans[item]))
    Translations.objects.create(
      english= en,
      hindi= hi,
      marathi= mr,
      telugu= te,
      punjabi= pa,
      file_id= fileId
    )
  logger.info('translated successfully')
  return {"status": "true"}


def google_translator_function(rows_data, target_language):
  api_key = env('GOOGLE_APPLICATION_CREDENTIALS')
  url = 'https://translation.googleapis.com/language/translate/v2?key={}'
  batchsize = 100
  data = [rows_data[item:item + batchsize] for item in range(0, len(rows_data), batchsize)]
  response_data= []
  for element in data:
    payload = {
      "q": element,
      "target": target_language,
      "source": 'en'
    }
    response = requests.post(url.format(api_key), data=payload)
    response_json = json.loads(response.content)
    response_data.extend([item['translatedText'] for item in response_json.get('data').get('translations')])
  response = [response_data[item:item + 5] for item in range(0, len(response_data), 5)]
  return response