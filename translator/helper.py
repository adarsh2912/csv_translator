import base64
import csv
from translator.models import File
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='tmp/')


def save_file_as_base64(content):
  """Saves binary encoded csv data into databse

  Args: 
      byte string object of csv file content

  Returns: 
      ObjectId: Document ObjectId of file.

  """
  base64_content = base64.b64encode(content)
  temp = File.objects.create(file_base64=base64_content)
  
  return str(temp._id)

def save_file_as_temp_csv(content):
  """Saves content as .csv in local tmp folder

  Args:
    Byte string: byte string object of csv file content

  Returns:
      string: string of file path

  """
  file_content = ContentFile(content)
  file_name = fs.save(
    "_tmp.csv", file_content
  )
  tmp_file = fs.path(file_name)

  return tmp_file

def get_csv_data(csv_file):
  """Return list of field name and all row data combine as list

  Args:
      str: file path csv saved in local memory
  
  Returns:
      List: list of csv field names
      List: list of all rows data combine

  """
  fieldName = []
  row_value = []
  with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    i = 0
    for row in reader:
      if i == 0:
        fieldName.extend(row)
        i = 1
      else:
        row_value.extend(row)
  return fieldName, row_value
