"""
Views for login
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login


def log_in(request):
    #pylint: disable=no-else-return,inconsistent-return-statements
    """
    Login and redirect to either application view or reviewer view depending on user type
    """
    if has_permission(request.user) is True:
        if request.method == 'POST':
            email = request.POST['email']
            passwort = request.POST['passwort']
            user = authenticate(username=email, password=passwort)
            if user is not None:
                login(request,user=user)
                return redirect(redirect_to(user))
            else:
                return render(request, 'login/login.html', {'success': False})
        else:
            return render(request, 'login/login.html')
    else:
        return redirect(redirect_to(request.user))


def redirect_to(user):
    """
    Returns string with the name of an url to redirect
    """
    if user.is_student is True:
        return 'applicant'
    if user.is_reviewer is True:
        return 'reviewer'
    
    return 'login'


def has_permission(user):
    """
    Checks if a user has permission to see the login page
    """
    try:
        return not any([user.is_student, user.is_reviewer])
    except AttributeError:
        return True
