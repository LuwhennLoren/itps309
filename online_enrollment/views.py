# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from .forms import RegisterForm
# from django.contrib.auth.decorators import login_required
# from .models import StudentInformation, StudentBackgroundInformation, StudentEducationalAttainment, StudentSubject
# from .forms import StudentInformationForm, StudentBackgroundForm, StudentEducationForm, StudentSubjectForm
# from django.views.decorators.cache import never_cache
# # Create your views here.

# @never_cache
# def register_user(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Account created successfully! You can now log in.')
#             return redirect('login_user')
#         else:
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})

# @never_cache
# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f'Welcome back, {username}!')
#                 return redirect('user_profile')
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Invalid input.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def logout_user(request):
#     logout(request)
#     messages.info(request, 'You have been logged out')
#     return redirect('login_user')

# @login_required
# def user_profile(request):
#     user = request.user

#     info = StudentInformation.objects.filter(user=user).first()
#     background = StudentBackgroundInformation.objects.filter(user=user).first()
#     education = StudentEducationalAttainment.objects.filter(user=user).first()
#     subjects = StudentSubject.objects.filter(user=user)

#     context = {
#         "info": info,
#         "background": background,
#         "education": education,
#         "subjects": subjects,
#     }

#     return render(request, "profile.html", context)

# @login_required
# def enrollment_form(request):
#     if request.method == "POST":
#         info_form = StudentInformationForm(request.POST)
#         bg_form = StudentBackgroundForm(request.POST)
#         edu_form = StudentEducationForm(request.POST)
#         sub_form = StudentSubjectForm(request.POST)

#         if info_form.is_valid() and bg_form.is_valid() and edu_form.is_valid() and sub_form.is_valid():
#             info_form.save()
#             bg_form.save()
#             edu_form.save()
#             sub_form.save()
#             return redirect("profile_view")  # after submission go to profile

#     else:
#         info_form = StudentInformationForm()
#         bg_form = StudentBackgroundForm()
#         edu_form = StudentEducationForm()
#         sub_form = StudentSubjectForm()

#     return render(request, "enrollment_form.html", {
#         "info_form": info_form,
#         "bg_form": bg_form,
#         "edu_form": edu_form,
#         "sub_form": sub_form,
#     })


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.forms import modelformset_factory

from .forms import (
    RegisterForm,
    StudentInformationForm,
    StudentBackgroundForm,
    StudentEducationForm,
    StudentSubjectForm,
)

from .models import (
    StudentInformation,
    StudentBackgroundInformation,
    StudentEducationalAttainment,
    StudentSubject,
)

# --------------------------------------------
# REGISTER (Block logged-in users + no cache)
# --------------------------------------------
@never_cache
def register_user(request):

    # Redirect logged-in users away from register
    if request.user.is_authenticated:
        return redirect('user_profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# --------------------------------------------
# LOGIN (Block logged-in users + no cache)
# --------------------------------------------
@never_cache
def login_user(request):
    if request.user.is_authenticated:
        return redirect('user_profile')

    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('user_profile')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {'form': form})


# --------------------------------------------
# LOGOUT
# --------------------------------------------
def logout_user(request):
    logout(request)  # logs the user out
    # Add a single message for the logout page only
    messages.success(request, "You’ve been logged out. Hope to see you again soon! 🌼")
    return render(request, "logout.html")


# --------------------------------------------
# PROFILE VIEW
# --------------------------------------------
@login_required
def user_profile(request):
    user = request.user

    context = {
        "info": StudentInformation.objects.filter(user=user).first(),
        "background": StudentBackgroundInformation.objects.filter(user=user).first(),
        "education": StudentEducationalAttainment.objects.filter(user=user).first(),
        "subjects": StudentSubject.objects.filter(user=user),
    }

    return render(request, "profile.html", context)


# --------------------------------------------
# ENROLLMENT FORM (Auto-link to logged-in user)
# --------------------------------------------
@login_required
def enrollment_form(request):

    # Load existing records if they exist
    info = StudentInformation.objects.filter(user=request.user).first()
    background = StudentBackgroundInformation.objects.filter(user=request.user).first()
    education = StudentEducationalAttainment.objects.filter(user=request.user).first()

    if request.method == "POST":
        info_form = StudentInformationForm(request.POST, request.FILES, instance=info)
        bg_form = StudentBackgroundForm(request.POST, instance=background)
        edu_form = StudentEducationForm(request.POST, instance=education)
        sub_form = StudentSubjectForm(request.POST)

        # --------------- ADD SUBJECT BUTTON ---------------
        if "add_subject" in request.POST:
            if sub_form.is_valid():
                subject = sub_form.save(commit=False)
                subject.user = request.user
                subject.save()
                messages.success(request, "Subject added! You can add another one.")
            sub_form = StudentSubjectForm()  # reset the subject form

        # --------------- SUBMIT ENROLLMENT BUTTON ---------------
        elif "submit_form" in request.POST:
            if (info_form.is_valid() and bg_form.is_valid() and
                edu_form.is_valid() and sub_form.is_valid()):

                info_obj = info_form.save(commit=False)
                info_obj.user = request.user
                info_obj.save()

                bg_obj = bg_form.save(commit=False)
                bg_obj.user = request.user
                bg_obj.save()

                edu_obj = edu_form.save(commit=False)
                edu_obj.user = request.user
                edu_obj.save()

                # Save last subject entry when user clicks submit
                sub_obj = sub_form.save(commit=False)
                sub_obj.user = request.user
                sub_obj.save()

                messages.success(request, "Enrollment submitted!")
                return redirect("user_profile")

    else:
        info_form = StudentInformationForm(instance=info)
        bg_form = StudentBackgroundForm(instance=background)
        edu_form = StudentEducationForm(instance=education)
        sub_form = StudentSubjectForm()

    return render(request, "enrollment_form.html", {
        "info_form": info_form,
        "bg_form": bg_form,
        "edu_form": edu_form,
        "sub_form": sub_form,
    })



@login_required
def edit_profile(request):
    info = StudentInformation.objects.filter(user=request.user).first()
    background = StudentBackgroundInformation.objects.filter(user=request.user).first()
    education = StudentEducationalAttainment.objects.filter(user=request.user).first()
    subjects = StudentSubject.objects.filter(user=request.user)

    SubjectFormSet = modelformset_factory(StudentSubject, form=StudentSubjectForm, extra=1, can_delete=True)
    
    if request.method == "POST":
        info_form = StudentInformationForm(request.POST, request.FILES, instance=info)
        bg_form = StudentBackgroundForm(request.POST, instance=background)
        edu_form = StudentEducationForm(request.POST, instance=education)
        formset = SubjectFormSet(request.POST, queryset=subjects)

        if info_form.is_valid() and bg_form.is_valid() and edu_form.is_valid() and formset.is_valid():
            info_form.save()
            bg_form.save()
            edu_form.save()
            formset.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        info_form = StudentInformationForm(instance=info)
        bg_form = StudentBackgroundForm(instance=background)
        edu_form = StudentEducationForm(instance=education)
        formset = SubjectFormSet(queryset=subjects)

    return render(request, "edit_profile.html", {
        "info_form": info_form,
        "bg_form": bg_form,
        "edu_form": edu_form,
        "formset": formset,
    })
