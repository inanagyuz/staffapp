import datetime
from django.db import models

# Create your models here.
class Staff(models.Model): 
    name = models.CharField(max_length=200,verbose_name="Adı", default="")
    surname = models.CharField(max_length=200,verbose_name="Soyadı",default="")
    idNumber = models.PositiveIntegerField(verbose_name="TC Kimlik No",default=False)
    dateofBirth = models.DateField(("Doğum Tarihi"), auto_now=False, auto_now_add=False, default=datetime.date.today,blank=True)
    title = models.CharField(max_length=250,verbose_name="Ünvan",default="",blank=True)
    phoneNumber = models.CharField(max_length=21,verbose_name="Cep Tel",default="",blank=True)
    emergencyPhoneNumber = models.CharField(max_length=21,verbose_name="Acil Durumda Aranacak Kişi Tel",default="",blank=True)
    email = models.EmailField(max_length=50,verbose_name="E-Posta",default="",blank=True)
    adress = models.TextField(verbose_name="Adres",default="",blank=True)
    county = models.CharField(max_length=200,verbose_name="İl",default="",blank=True)
    district = models.CharField(max_length=200,verbose_name="İlçe",default="",blank=True)
    description = models.TextField(verbose_name="Açıklama",default="",blank=True)
    projectName = models.ForeignKey('Project', default=1, on_delete=models.SET_DEFAULT, verbose_name="Proje",blank=True)
    dateEntry = models.DateField(("Giriş Tarihi"), auto_now=False, auto_now_add=False, default=datetime.date.today,blank=True)
    releaseDate = models.DateField(("Çıkış Tarihi"), auto_now=False, auto_now_add=False, default=datetime.date.today,blank=True)
    bloodgroup_choise = [
        ("0", '0 Rh(-)'),
        ("00", '0 Rh(+)'),
        ("A", 'A Rh(-)'),
        ("AA", 'A Rh(+)'),
        ("B", 'B Rh(-)'),
        ("BB", 'B Rh(+)'),
        ("AB", 'AB Rh(-'),
        ("AABB", 'AB Rh(+)'),
    ]
    bloodgroup = models.CharField(max_length=10,choices=bloodgroup_choise, default="",verbose_name="Kan Grubu",blank=True)
    is_active = models.BooleanField(verbose_name="Aktif", default=False)
   
    


    def __str__(self) : 
        return f'{self.name + " " + self.surname}'


class Project(models.Model):
    projectName = models.CharField(max_length=200, verbose_name="Proje Adı",default="")
    customerName = models.CharField(max_length=200,verbose_name="Müşteri İsmi",default="")
    customerPhone = models.CharField(max_length=200, verbose_name="Müşteri Telefon Numarası",default="")
    customerMail = models.EmailField(max_length=200,verbose_name="Müşteri E-postası", default="")
    projectAdress = models.TextField(verbose_name="Proje Adresi",default="")
    projectManager = models.ForeignKey(Staff, default=1, on_delete=models.SET_DEFAULT, verbose_name="Proje Yöneticisi")

    def __str__(self):
        return f"{self.projectName}"