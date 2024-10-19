from django.db import models

# Create your models here.
from django.db import models

class VentFindings(models.Model):
    BREED_CHOICES = [
        ('Berkshire', 'Berkshire'),
        ('Duroc', 'Duroc'),
        ('Yorkshire', 'Yorkshire'),
        ('Landrace', 'Landrace'),
        ('Tamworth', 'Tamworth'),
        ('Large Black', 'Large Black'),
        ('Vietnamese Potbelly', 'Vietnamese Potbelly'),
        ('Juliana', 'Juliana'),
        ('Pietrain', 'Pietrain'),
        ('Chester White', 'Chester White'),
    ]
    AGE_CHOICES = [
        ('young', 'Young'),
        ('medium', 'Medium'),
        ('old', 'Old'),
    ]

    DISEASE_CHOICES = [
        ('Swine Flu', 'Swine Flu'),
        ('African Swine Fever', 'African Swine Fever'),
        ('Porcine Reproductive and Respiratory Syndrome (PRRS)', 'PRRS'),
        ('Porcine Parvovirus', 'Porcine Parvovirus'),
        ('Leptospirosis', 'Leptospirosis'),
        ('Foot and Mouth Disease', 'Foot and Mouth Disease'),
        ('Transmissible Gastroenteritis', 'Transmissible Gastroenteritis'),
        ('Actinobacillus pleuropneumonia', 'Actinobacillus pleuropneumonia'),
        ('Erysipelas', 'Erysipelas'),
    ]

    type_of_breed = models.CharField(max_length=100, choices=BREED_CHOICES)
    age = models.CharField(max_length=100,choices=AGE_CHOICES)
    type_of_disease = models.CharField(max_length=100, choices=DISEASE_CHOICES)
    symptoms = models.TextField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.type_of_disease
   
class FarmerRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
     
    def __str__(self):
        return self.phone_number