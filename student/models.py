from django.db import models


# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    Adhar_Card_Number = models.IntegerField()
    DOB = models.DateField()
    Identification_Marks = models.CharField(max_length=500)
    Category = models.CharField(max_length=10,choices=GENDER_CHOICES)
    Height = models.FloatField()
    Weight = models.FloatField()
    Mail_Id = models.EmailField()
    Contact_Detail = models.IntegerField()
    Address = models.CharField(max_length=1000)
    
    Fathers_Name = models.CharField(max_length=100)
    Fathers_Qualification = models.CharField(max_length=100)
    Fathers_Profession = models.CharField(max_length=100)
    Fathers_Designation = models.CharField(max_length=100)
    Fathers_Aadhar_Card = models.IntegerField()
    Fathers_Mobile_Number = models.IntegerField()
    Fathers_Mail_Id = models.EmailField()
    Mothers_Name = models.CharField(max_length=100)
    Mothers_Qualification = models.CharField(max_length=100)
    Mothers_Profession = models.CharField(max_length=100)
    Mothers_Designation = models.CharField(max_length=100)
    Mothers_Aadhar_Card = models.IntegerField()
    Mothers_Mobile_Number = models.IntegerField()
    Mothers_Mail_Id = models.EmailField()
    
    enrollment_date = models.DateField(auto_now_add=True)
    Enrollment_ID = models.CharField(max_length=12, unique=True)
    Class = models.CharField(max_length=10)
    Section = models.CharField(max_length=10)
    DOJ = models.DateField()

    adhaar_card = models.FileField(upload_to='documents/')
    poa_document = models.FileField(upload_to='documents/')
    poi_document = models.FileField(upload_to='documents/')
    tc_document = models.FileField(upload_to='documents/')
    certificate = models.FileField(upload_to='documents/')
    
    def __str__(self) -> str:
        return self.Name