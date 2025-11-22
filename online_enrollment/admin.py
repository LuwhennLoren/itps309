from django.contrib import admin
from .models import StudentAccount, StudentInformation, StudentSubject, StudentBackgroundInformation, StudentEducationalAttainment
# Register your models here.

admin.site.register(StudentAccount)
admin.site.register(StudentInformation)
admin.site.register(StudentSubject)
admin.site.register(StudentBackgroundInformation)
admin.site.register(StudentEducationalAttainment)

