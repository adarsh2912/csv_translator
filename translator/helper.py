import base64
from translator.models import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='tmp/')

def save_file_as_base64(content):
  base64_content = base64.b64encode(content)
  temp = File.objects.create(file_base64=base64_content)

  return temp._id

def save_file_as_temp_csv(content):
  file_content = ContentFile(content)
  file_name = fs.save(
    "_tmp.csv", file_content
  )
  tmp_file = fs.path(file_name)

  return tmp_file