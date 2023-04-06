import datetime
from django.utils import timezone
from django.db import models
from staff.models import Project, Staff

# Create your models here.
class TrainingDefinition(models.Model):
    trainingName = models.CharField(max_length=200, verbose_name="Eğitim Adı",default="")
    trainingdesc = models.TextField(max_length=200, verbose_name="Eğitim Açıklaması",default="")
    preparedTraining = models.CharField(max_length=200, verbose_name="Eğitimi Hazırlayan",default="")
    preparationDate = models.DateField(("Hazırlama tarihi"), auto_now=False, auto_now_add=False, default=datetime.date.today)
   
    def __str__(self):
        return f"{self.trainingName}"

class Training(models.Model):
    projectName = models.ForeignKey(Project, default=1, on_delete=models.SET_DEFAULT, verbose_name="Proje",max_length=200)
    trainingName = models.ForeignKey('TrainingDefinition', default=1, on_delete=models.SET_DEFAULT, verbose_name="Eğitim")
    providingTraining = models.CharField(max_length=200, verbose_name="Eğitimi Veren", default="")
    trainingStartDate = models.DateTimeField("Eğitim Başlama Tairihi", auto_now=False,auto_now_add=False,default=timezone.now)     
    trainingEndDate = models.DateTimeField("Eğitim Bitiş Tarihi", auto_now=False,auto_now_add=False,default=timezone.now)    
    trainingTime = models.CharField(max_length=200, verbose_name="Eğitim Süresi",default="")
    trainingStatus_choise = [
        ("PLANLANDI", 'Planlandı'),
        ("GERCEKLESTI", 'Gerçekleşti'),
        ("BASLADI", 'Başladı'),
        ("DEVAMEDIYOR", 'Devam Ediyor'),
    ]
    trainingStatus = models.CharField(max_length=50,choices=trainingStatus_choise, default="",verbose_name="Eğitim Durumu")
    description = models.TextField(verbose_name="Açıklama",default="", blank=True)
    participants = models.ManyToManyField(Staff, verbose_name="Katılımcılar", default=[0] )

    def __str__(self):
        return f"{self.trainingName}"
    
    

