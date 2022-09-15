from django.db import models

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=227)
    email = models.CharField(max_length=227)
    gender = models.CharField(max_length=227)
    blood = models.CharField(max_length=227)
    is_active = models.BooleanField()


    def __str__(self):
        return self.name

class post(models.Model):
    title = models.CharField(max_length=225)
    content = models.TextField()
    #create_date_time = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(person,on_delete=models.CASCADE)

    def __str__(self):
        return self.title