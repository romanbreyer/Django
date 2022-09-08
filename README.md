<p align="center"><img src="https://abload.de/img/unikoeln_logoz0jg9.png" alt="Mark Text" width="100" height="100"></p>

<h1 align="center">SAMS</h1>

A simple   **S**tudent **A**pplication **M**anagement **S**ystem for the University of Cologne by Team Unchained.

# Installation
1. Clone this repository: `git clone https://github.com/uzk-swt-ws20/hausaufgabe1-zeitschatzung-zeitplanung-und-teamarbeit-unchained`
2. Install requirements `pip install -r requirements.txt`
3. cd into `sams`
4. Start Django `python manage.py runserver`
5. Project is now running on `http://127.0.0.1:8000/`

 SAMS requires [Python](https://www.python.org/) v3+ to run.
 
 
 # How to use
### Student

#### How to login
<img src="https://abload.de/img/loginpage_unchained5pjnh.png" width="600px">

1. Go to http://127.0.0.1:8000/
2. Enter E-Mail Address & Password
4. Press "Einloggen"
5. You will be redirected to http://127.0.0.1:8000/applicant/

#### How to register
<img src="https://abload.de/img/registerpage_unchainerwj6h.png" width="600px">

1. Go to http://127.0.0.1:8000/register
2. Enter E-Mail Address, Password, First Name, Last Name and your Grade
3. Select your educational qualification and select "Ja" if you have international experience
5. If you have a recommandation letter (.PDF file), you can upload it by pressing "Datei auswählen"
6. Press "Registrierung abschließen"
7. You are now logged in and you will be redirected to http://127.0.0.1:8000/applicant

#### How to apply
<img src="https://abload.de/img/applicantocj84.png" width="600px">
<img src="https://abload.de/img/applicant_bwercqjuc.png" width="600px">

1. You need to be logged in as an Applicant
2. Go to http://127.0.0.1:8000/applicant
3. In the navigation bar, select "Bewerben"
4. Now you can apply for Informatics by pressing the button "Bewerben" in the middle of the page
5. Successfully applied for Informatics!
6. To see the status of your application, go back to the main page ("Startseite")

#### Example Student Accounts for Testing
| E-Mail        | Passwort      |
| ------------- |:-------------:|
| max.mustermann@examplemail.de      | maxmuster123 |
| erika.musterfrau@examplemail.de | erikamuster123      |
| hans.peter@examplemail.de | hans123      |
| michelle.schmidt@examplemail.de | michelle123      |
| angelika.backer@examplemail.de | angelika123      |

---

### Reviewer
#### How to login
<img src="https://abload.de/img/loginpage_unchained5pjnh.png" width="600px">

1. Go to <span style="color:blue">http://127.0.0.1:8000/</span>
2. Enter E-Mail Address & Password
4. Press "Einloggen"
5. You will be redirected to http://127.0.0.1:8000/reviewer

#### How to register

You can't register a reviewer account on the front page like a normal user because a reviewer has special rights and needs to be created by the admin. See example reviewer accounts for credentials.

You can also create an own reviewer account on http://127.0.0.1:8000/admin by logging in and clicking Users -> "Add User" -> check "is_reviewer" and uncheck "is_student" and press "Save". There is one main admin account:

| E-Mail        | Passwort      |
| ------------- |:-------------:|
| unchained@examplemail.de      | root |

#### How to accept/reject an Application
<img src="https://abload.de/img/reviewer_pagelyktz.png">

1. You need to be logged in as a Reviewer
2. Go to http://127.0.0.1:8000/reviewer
3. To accept an Application, press the button "Akzeptieren", to reject an Application, press the button "Ablehnen"
4. To see open applications, press "Offen", to see accepted applications, press "Angenommen", to see rejected applications, press "Abgelehnt"

#### Example Reviewer Accounts for Testing


| E-Mail        | Passwort      |
| ------------- |:-------------:|
| reviewer1@examplemail.de      | reviewerpass1 |
| reviewer2@examplemail.de | reviewerpass2      |


# Quality Check

Testing was implemented with Pylint 2.6.0 and Pylint-django 2.3.0

<img src="https://image.prntscr.com/image/auPmUAJKS16NJpO1dnk2jg.png">
