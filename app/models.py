from django.db import models

# Create your models here.
class person(models.Model):
    p_name=models.CharField(max_length=40)
    p_address=models.CharField(max_length=30)
    p_phone=models.CharField(max_length=17)
    
    
    def __str__(self):
        return str(self.p_name)