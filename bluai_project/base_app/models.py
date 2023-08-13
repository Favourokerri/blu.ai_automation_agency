from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Hero_section(models.Model):
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=200)

class About_us(models.Model):
    about=RichTextField(default="syllabus")
