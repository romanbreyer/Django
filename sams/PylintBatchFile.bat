rem applicant
echo [1mPylint results for applicant/views.py[0m
pylint --load-plugins pylint_django applicant/views.py
echo.
echo [1mPylint results for applicant/models.py[0m
pylint --load-plugins pylint_django applicant/models.py
echo.

rem login
echo [1mPylint results for login/views.py[0m
pylint --load-plugins pylint_django login/views.py
echo.
echo [1mPylint results for login/models.py[0m
pylint --load-plugins pylint_django login/models.py
echo.

rem registrierung
echo [1mPylint results for registrierung/views.py[0m
pylint --load-plugins pylint_django registrierung/views.py
echo.
echo [1mPylint results for registrierung/models.py[0m
pylint --load-plugins pylint_django registrierung/models.py
echo.

rem reviewer
echo [1mPylint results for reviewer/views.py[0m
pylint --load-plugins pylint_django reviewer/views.py
echo.
echo [1mPylint results for reviewer/models.py[0m
pylint --load-plugins pylint_django reviewer/models.py
echo.

rem manage.py
echo [1mPylint results for manage.py[0m
pylint --load-plugins pylint_django manage.py
echo.