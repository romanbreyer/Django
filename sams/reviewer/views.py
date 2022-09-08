"""
Views for reviewer
"""
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from applicant.models import Application


def reviewer(request):
    #pylint: disable=no-else-return
    """
    Renders the reviewer HTML template
    """
    if has_permission(request.user) is True:
        if request.method == 'POST':
            if request.POST['fromNavBar'] == 'False':
                update_application(request)
        return render(request, 'reviewer/reviewer.html', get_context(request))
    else:
        return redirect('login')


def get_context(request):
    """
    Return the context used in the HTML templates
    """
    if request.method == 'GET':
        status = 0
    elif request.method == 'POST':
        status = int(request.POST['status'])

    applications = sort_by_score(Application.objects.filter(status=status))
    open_applications_length = len(Application.objects.filter(status=0))
    accepted_applications_length = len(Application.objects.filter(status=1))
    rejected_applications_length = len(Application.objects.filter(status=2))
    total_applications_length = len(Application.objects.all())

    return {
        'applications': applications,
        'status': status,
        'open_applications_length': open_applications_length,
        'accepted_applications_length': accepted_applications_length,
        'rejected_applications_length': rejected_applications_length,
        'total_applications_length': total_applications_length,
    }


def update_application(request):
    """
    Updates the status of an application
    """
    accept_application = request.POST['accept'] == 'yes'
    application = Application.objects.get(id=int(request.POST['applicationId']))

    if accept_application is True:
        application.status = 1
    elif accept_application is False:
        application.status = 2
    application.save()


def sort_by_score(applications):
    """
    Sorts applications by score attribute
    """
    return sorted(applications, key=lambda  a: a.score)


def log_out(request):
    """
    Logout function for a Reviewer
    """
    logout(request)
    return redirect('login')


def has_permission(user):
    """
    Checks if the user has permission to see the reviewer page
    """
    try:
        return user.is_reviewer
    except AttributeError:
        return False
