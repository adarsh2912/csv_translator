from django.http import JsonResponse
from translator.helper import (
  save_file_as_base64, 
  save_file_as_temp_csv
)

def upload_csv(request):
  if request.method == 'POST':
    file = request.FILES['file']
    content = file.read()
    file_id = save_file_as_base64(content)
    csv_file = save_file_as_temp_csv(content)
    
  
  return JsonResponse({'msg':'uploaded succesfully'})
