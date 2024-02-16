from django.db import models
from jsonfield import JSONField
from django.db import models
class Formtitle(models.Model):
    Form_name =models.CharField(max_length=1000)
    User_id=models.IntegerField()
    Form_Url=models.CharField(max_length=100)
    def __str__(self):
        return self.Form_name




class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    Form = models.ForeignKey(Formtitle, on_delete=models.CASCADE)
    question=models.CharField(max_length=10000)
    answer=JSONField(max_length=20000)
    type=models.CharField(max_length=100)
    option1=models.CharField(max_length=100,blank=True)
    option2=models.CharField(max_length=100,blank=True)
    option3=models.CharField(max_length=100,blank=True)
    option4=models.CharField(max_length=100,blank=True)    
    def __str__(self):
        return self.question


class FormResponse(models.Model):
    form = models.ForeignKey(Formtitle, on_delete=models.CASCADE)
    submit_time = models.DateTimeField(auto_now_add=True)
    form_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    response_user_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.form_name} submitted by {self.response_user_id}"

