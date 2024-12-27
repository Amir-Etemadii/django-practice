from django.db import models

class Course(models.Model):
    title= models.CharField(max_length=50)
    body= models.TextField()
    photo= models.ImageField(upload_to='img/courses')
    status= models.BooleanField(default=False)
    view= models.IntegerField(default=0)
    teacher_nama= models.CharField(max_length=80)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


