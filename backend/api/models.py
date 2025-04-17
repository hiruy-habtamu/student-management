from django.db import models
class Batch(models.Model):
    year = models.PositiveSmallIntegerField()

class Dorm(models.Model):
    building = models.PositiveSmallIntegerField()
    floor = models.PositiveSmallIntegerField()
    dorm = models.PositiveSmallIntegerField()

class Student(models.Model):

    SEX_CHOICES = {
        "F" : "Female",
        "M" : "MALE"
    }

    admission_number = models.PositiveIntegerField(null=True)
    university_id = models.PositiveBigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35,null=True)
    sex = models.CharField(max_length=1,choices=SEX_CHOICES)
    email = models.EmailField(unique=True)
    section = models.CharField(max_length=3,null=True)
    batch = models.ForeignKey(Batch,on_delete=models.PROTECT)
    dorm = models.ForeignKey(Dorm,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='students/images/',null=True,blank=True)
    matric_pdf = models.FileField(upload_to='students/pdfs',null=True,blank=True)

    #To not reproduce the same email
    def generate_unique_email(self):
        base_email = f"{self.first_name.lower()}{self.last_name.lower()}@aastu.edu.et"
        email = base_email
        counter = 1

        while Student.objects.filter(email=email).exists():
            email = f"{self.first_name.lower()}{self.last_name.lower()}{counter}@aastu.edu.et"
            counter += 1

        return email

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = self.generate_unique_email()
        super().save(*args, **kwargs)