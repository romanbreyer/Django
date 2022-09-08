bold=$(tput bold)
normal=$(tput sgr0)

# applicant
echo "${bold}Pylint results for applicant/views.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django applicant/views.py
echo "${bold}Pylint results for applicant/models.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django applicant/models.py

# login
echo "${bold}Pylint results for login/views.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django login/views.py
echo "${bold}Pylint results for login/models.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django login/models.py

# registrierung
echo "${bold}Pylint results for registrierung/views.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django registrierung/views.py
echo "${bold}Pylint results for registrierung/models.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django registrierung/models.py

# reviewer
echo "${bold}Pylint results for reviewer/views.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django reviewer/views.py
echo "${bold}Pylint results for reviewer/models.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django reviewer/models.py

# manage.py
echo "${bold}Pylint results for manage.py${normal}"
DJANGO_SETTINGS_MODULE=sams/settings.py pylint --load-plugins pylint_django manage.py