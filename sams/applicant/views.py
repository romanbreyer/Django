"""
Views for applicant
"""
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from applicant.models import Application

def applicant(request):
    #pylint: disable=no-else-return
    """
    Redirect to login if user is not applicant
    Else show applicant view
    """
    try:
        if request.user.is_student is True:
            return render(request, 'applicant/applicant.html', {'status': get_status(request)})
        else:
            return redirect('login')
    except AttributeError:
        return redirect('login')


def bewerben(request):
    # pylint: disable=no-else-return
    """
    Redirect to login if user is not applicant
    Else if user has applied already show status, else show button 'bewerben'
    """
    try:
        if request.user.is_student is True:
            if get_status(request) is None:
                if request.method == 'POST':
                    application = Application(status=0, applicant=request.user)
                    application.save()
                    return render(request,
                                  'applicant/bewerben.html',
                                  {'success': True, 'status': get_status(request)})
                else:
                    return render(request,
                                  'applicant/bewerben.html',
                                  {'status': get_status(request)})
            else:
                return redirect('applicant')
        else:
            return redirect('login')
    except AttributeError:
        return redirect('login')


def daten(request):
    # pylint: disable=no-else-return
    """
    Redirect to login if user is not applicant
    Else show user data
    """
    try:
        if request.user.is_student is True:
            return render(request,
                          'applicant/daten.html',
                          {'status': get_status(request)})
        else:
            return redirect('login')
    except AttributeError:
        return redirect('login')


def log_out(request):
    """
    Logout
    """
    try:
        logout(request)
        return redirect('login')
    except AttributeError:
        return redirect('login')


def get_status(request):
    # pylint: disable=no-else-return
    """
    Get status of application from applicant
    """
    try:
        application = Application.objects.get(applicant=request.user)
        if application:
            return application.status
        else:
            return None
    except Application.DoesNotExist:
        return None
