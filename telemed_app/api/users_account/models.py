from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from api.patient_record.models import PatientRecord

# Create your models here.
class TeleMedUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = CustomUserManager


    def __str__(self) -> str:
        return self.email
    

    @property
    def is_staff(self):
        return self.is_admin
    



class DocSpecialty(models.Model):
   DOC_SPECIALTY = [
        ('INTERNAL MEDICINE', 'Internal Medicine'),
        ('PEDIATRICIAN', 'Pediatrician'),
        ('ORTHOPEDIST', 'Orthopedist'),
        ('PSYCHIATRIST', 'Psychiatrist'),
        ('UROLOGIST', 'Urologist'),
        ('PATHOLOGIST', 'Pathologist'),
        ('NEUROLOGIST', 'Neurologist'),
        ('GASTROENTEROLOGIST', 'Gastroenterologist'),
        ('ANESTHESIOLOGIST', 'Anesthesiologist'),
        ('OBSTERICIAN', 'Obsterician'),
        ('GYNAECOLOGIST', 'Gynaecologist'),
        ('DERMATOLOGIST', 'Dermatologist'),
        ('RHEUMATOLOGIST', 'Rheumatologist'),
        ('OPHTHALMOLOGIST', 'Ophthalmologist'),
        ('CARDIOLOGIST', 'Cardiologist'),
        ('FAMILY MEDICINE', 'Family Medicine'),
        ('RADIOLOGIST', 'Radiologist'),
        ('NEUROLOGIST', 'Neurologist'),
        ('ONCOLOGIST', 'Oncologist'),
        ('NEPHEROLOGIST', 'Nepherologist'),
    ]
   specialty = models.CharField(max_length=30, choices=DOC_SPECIALTY, default='FAMILY MEDICINE')
   
   def __str__(self):
       return self.specialty
   


class Doctor(models.Model):
    LANGUAGE = [
        ('English', 'English'),        
        ('Hausa', 'Hausa'),
        ('Igbo', 'Igbo'),
        ('Yoruba', 'Yoruba'),
    ]
    doctor = models.OneToOneField(TeleMedUser, on_delete=models.CASCADE)
    specialty = models.ForeignKey(DocSpecialty, related_name='doc_specialty', on_delete=models.CASCADE)
    language = models.CharField(max_length=15, choices=LANGUAGE, default='ENGLISH')
    location = models.CharField(max_length=20)
    Hospital = models.CharField(max_length=30)
    years_of_experience = models.CharField(max_length=2)
    about = models.TextField()
    date_modified = models.DateTimeField(TeleMedUser, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f'{self.doctor.first_name} {self.doctor.last_name}'
    


class Patient(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Others',  'Others')
    ]
    patient = models.OneToOneField(TeleMedUser, on_delete=models.CASCADE)
    patient_record = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7, choices=GENDER, default='Others')
    alternateive_phone = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=30)
    emergency_contact_phone = models.CharField(max_length=15)
    emergency_contact_relationship =models.CharField(max_length=20)
    medical_plan = models.CharField(max_length=20)
    nin = models.IntegerField()
    date_modified = models.DateTimeField(TeleMedUser, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return f'{self.patient.first_name} {self.patient.last_name}'


# Create Doctors and Patients' Profile using their respective models with post_save signal
    