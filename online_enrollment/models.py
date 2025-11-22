from django.db import models
from django.contrib.auth.models import User

# Student Account - only extra fields (Django handles username/email/password)
class StudentAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    student_id = models.IntegerField()
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}"

# Student Personal Information
class StudentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    age = models.IntegerField()
    nationality = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default="img/default_profile.png")


    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

# Student Subjects
class StudentSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject_code = models.CharField(max_length=50)
    subject_description = models.CharField(max_length=70)
    unit = models.IntegerField()
    day = models.CharField(max_length=10)
    professor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.subject_code}"

# Student Background Information
class StudentBackgroundInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mother_maiden_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    guardian_name = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.guardian_name}"

# Student Educational Attainment
class StudentEducationalAttainment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    elementary_school = models.CharField(max_length=50)
    HS_school = models.CharField(max_length=50)
    SHS_school = models.CharField(max_length=50)
    College_school = models.CharField(max_length=50)
    elementary_award = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.College_school}"
