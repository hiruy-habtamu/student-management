from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
class User(AbstractUser):
    # Make email as a default login method
    USERNAME_FIELD = 'email'
    # Should remove email from REQUIRED_FIELDS cuz IDK why
    REQUIRED_FIELDS = []
    # It asks me to make User.email a unique field cuz it is named as USERNAME_FIELD
    email = models.EmailField(unique=True)

class Batch(models.Model):
    year = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"{self.year} Batch"


class Dorm(models.Model):
    building = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    room = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Block {self.building}, {self.room}"

class Student(models.Model):

    SEX_CHOICES = {
        "F" : "Female",
        "M" : "Male"
    }
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    admission_number = models.PositiveIntegerField(null=True)
    university_id = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35,null=True)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    section = models.CharField(max_length=3,null=True)
    batch = models.ForeignKey(Batch,on_delete=models.PROTECT)
    dorm = models.ForeignKey(Dorm,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='students/images/',null=True,blank=True)
    matric_pdf = models.FileField(upload_to='students/pdfs',null=True,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    #To not reproduce the same email and generate email automatically
    def default_email(self):
        email = f"{self.first_name.lower()}.{self.last_name.lower()}@aastustudent.edu.et"
        counter = 1

        while Student.objects.filter(email=email).exists():
            email = f"{self.first_name.lower()}.{self.last_name.lower()}{counter}@aastustudent.edu.et"
            counter += 1

        return email
    
    email = models.EmailField(unique=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.default_email()
        # Need to create an api_user that is non-admin user for authentication purposes
        if not self.user:
            # Only create the user if it doesn't already exist
            user = User.objects.create_user(
                username=f'{self.first_name}.{self.last_name}.{self.university_id}',
                email=self.email,
                password='12345678'
            )
            user.save()
            self.user = user
        super().save(*args, **kwargs)