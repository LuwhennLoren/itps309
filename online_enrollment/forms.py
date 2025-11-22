from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentInformation, StudentBackgroundInformation, StudentEducationalAttainment, StudentSubject
from django.forms import modelformset_factory

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentInformationForm(forms.ModelForm):
    class Meta:
        model = StudentInformation
        fields = ['firstname', 'middlename', 'lastname', 'age', 'nationality', 'profile_image']

class StudentBackgroundForm(forms.ModelForm):
    class Meta:
        model = StudentBackgroundInformation
        fields = ['mother_maiden_name', 'father_name', 'guardian_name', 'mother_occupation', 'father_occupation']

class StudentEducationForm(forms.ModelForm):
    class Meta:
        model = StudentEducationalAttainment
        fields = ['elementary_school', 'HS_school', 'SHS_school', 'College_school', 'elementary_award']

class StudentSubjectForm(forms.ModelForm):
    class Meta:
        model = StudentSubject
        fields = ['subject_code', 'subject_description', 'unit', 'day', 'professor']

# Formset
StudentSubjectFormSet = modelformset_factory(StudentSubject, form=StudentSubjectForm, extra=0, can_delete=True)