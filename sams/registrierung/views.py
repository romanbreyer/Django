"""
Views for registrierung
"""
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from login.models import User


def registrierung(request):
    #pylint: disable=no-else-return, broad-except, inconsistent-return-statements
    """
    Create applicant account
    """
    try:
        if request.user.is_student is True:
            return redirect('applicant')
        elif request.user.is_reviewer is True:
            return redirect('reviewer')
    except AttributeError:
        if request.method == 'POST':
            try:
                email = request.POST['email']
                passwort = make_password(request.POST['passwort'])

                first_name = request.POST['first_name']
                last_name = request.POST['last_name']

                try:
                    empfehlungsschreiben = request.FILES['empfehlungsschreiben']
                    file_system_storage = FileSystemStorage()
                    file_system_storage.save(empfehlungsschreiben.name, empfehlungsschreiben)
                except MultiValueDictKeyError:
                    empfehlungsschreiben = None

                abschluss = request.POST['abschluss']
                note = float(request.POST['note'])
                auslandserfahrung = request.POST['auslandserfahrung'] == 'ja'

                student = User(
                    username=email,
                    password=passwort,
                    first_name=first_name,
                    last_name=last_name,
                    abschluss=abschluss,
                    note=note,
                    empfehlungsschreiben=empfehlungsschreiben,
                    auslandserfahrung=auslandserfahrung,
                )
                student.save()
                login(request, student)
                return redirect('applicant')
            except Exception as error:
                return render(request,
                              'registrierung/registrierung.html',
                              {'success': False, 'error': error})
            return render(request, 'registrierung/registrierung.html')
        else:
            return render(request, 'registrierung/registrierung.html')
