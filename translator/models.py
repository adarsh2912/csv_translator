from djongo import models

# Create your models here.
class File(models.Model):
  _id = models.ObjectIdField()
  file_base64 = models.TextField()

class FarmerDetails(models.Model):
  phone_number = models.CharField(max_length=15)
  farmer_name = models.CharField(max_length=200)
  state_name = models.CharField(max_length=200)
  district_name = models.CharField(max_length=200)
  village_name = models.CharField(max_length=200)

  class Meta:
    abstract = True

class Translations(models.Model):
  _id = models.ObjectIdField()
  english = models.EmbeddedField(
        model_container=FarmerDetails
  )
  hindi = models.EmbeddedField(
        model_container=FarmerDetails
  )
  marathi = models.EmbeddedField(
        model_container=FarmerDetails
  )
  telugu = models.EmbeddedField(
        model_container=FarmerDetails
  )
  punjabi = models.EmbeddedField(
        model_container=FarmerDetails
  )
  file_id = models.CharField(max_length=24)
