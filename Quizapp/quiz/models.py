from django.db import models

class quiz(models.Model):
    question=models.TextField()
    a=models.TextField()
    b=models.TextField()
    c=models.TextField()
    d=models.TextField()
    correct=models.CharField(max_length=3)
    
    class Meta:
        db_table = 'quiz'
