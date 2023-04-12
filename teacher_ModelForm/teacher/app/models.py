from django.db import models

# Create your models here.
gender = (
    ('Male','Male'),
    ('Female','Female'),
)

class Teacher(models.Model):
    name = models.CharField(max_length=100,blank=True)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=100,choices=gender)
    hobby = models.CharField(max_length=50)
    image = models.ImageField(upload_to='teacher/',blank=True)
