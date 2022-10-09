from djongo import models

# Create your models here.
class File(models.Model):
  _id = models.ObjectIdField()
  file_base64 = models.TextField()
