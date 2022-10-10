from django.http import JsonResponse
from .tasks import translate_csv_data
from translator.helper import ( 
  save_file_as_temp_csv,
  get_csv_data,
  save_file_as_base64
)
from django.views.decorators.http import require_http_methods

@require_http_methods(['POST'])
def upload_csv(request):
  file = request.FILES['file']
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
