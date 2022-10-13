from django.http import JsonResponse
from .tasks import translate_csv_data
from translator.helper import ( 
  save_file_as_temp_csv,
  get_csv_data,
  save_file_as_base64
)
from .models import Translations
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def upload_csv(request):
  """Converts the csv to base64 and save it to DB

  Args: 
      FILE - csv file with request body.

  Returns: 
      Json-object with status_code 202-Accepted
      
  """
  try:
    file = request.FILES.get('file') 
    content = file.read()
    file_id = save_file_as_base64(content)
    csv_file = save_file_as_temp_csv(content)
    fieldName, rows_data = get_csv_data(csv_file)
    job = translate_csv_data.delay(fieldName, rows_data, file_id)
    response = {
      'msg': 'uploaded successfully',
      'file_id': file_id,
      'job_id': job.id
    }
    return JsonResponse(response, status=202)
  except:
    response = {
      'msg': 'unable to move ahead'
    }
    return JsonResponse(response, status=500)

@require_http_methods(['GET'])
def get_translated_data(request, id):
  """Returns translated data of csv file

  Args:
      id - objectId of file

  Returns:
      List of Json object containing each rows with translations

  """
  data = Translations.objects.filter(file_id=id)
  model_to_dict=[model for model in data.values()]
  for item in model_to_dict:
    item['_id'] = str(item.get('_id'))

  return JsonResponse(model_to_dict, safe=False, json_dumps_params={'ensure_ascii': False}, status=200)



