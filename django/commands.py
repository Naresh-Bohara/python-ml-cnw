'''
# Django Setup Commands (From Start to Showing index.html)

1. Create virtual environment
   python -m venv myenv

2. Activate virtual environment

Windows:
.\myenv\Scripts\activate

Mac / Linux:
source myenv/bin/activate

3. Install Django
   pip install django

4. Create Django project
   django-admin startproject myproject .

5. Run server (check installation)
   python manage.py runserver

6. Create Django app
   python manage.py startapp app

7. Register the app in settings.py

INSTALLED_APPS = [
'app',
]

8. Create templates folder

project structure:

myproject/
app/
templates/
index.html

9. Tell Django where templates are (settings.py)

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [BASE_DIR / 'templates'],
'APP_DIRS': True,
}
]

10. Create index.html

templates/index.html

<html>
<head>
    <title>Django Home</title>
</head>
<body>
    <h1>Hello Django</h1>
</body>
</html>

11. Create view

app/views.py

from django.shortcuts import render

def home(request):
return render(request, "index.html")

12. Create app urls

app/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name="home"),
]

13. Connect app urls to project

myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('app.urls')),
]

14. Run server

python manage.py runserver

15. Open browser

http://127.0.0.1:8000/

Now index.html will be shown.


'''

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
# ================================================
# DJANGO SETUP SCRIPT - Creates project and shows index.html
# ================================================

# 1. Create virtual environment
python -m venv myenv

# 2. Activate virtual environment
.\myenv\Scripts\Activate.ps1

# 3. Install Django
pip install django

# 4. Create Django project in current directory
django-admin startproject myproject .

# 5. Create app
python manage.py startapp app

# 6. Add 'app' to INSTALLED_APPS in settings.py
$settingsPath = "myproject\settings.py"
$appEntry = "    'app',"
(Get-Content $settingsPath) -replace "INSTALLED_APPS = \[", "INSTALLED_APPS = [`r`n$appEntry" | Set-Content $settingsPath

# 7. Create templates folder and index.html
New-Item -ItemType Directory -Path app\templates -Force
@"
<!DOCTYPE html>
<html>
<head>
    <title>My Django Page</title>
</head>
<body>
    <h1>Hello from Django!</h1>
</body>
</html>
"@ | Out-File -FilePath app\templates\index.html -Encoding utf8

# 8. Create urls.py in app folder
@"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"@ | Out-File -FilePath app\urls.py -Encoding utf8

# 9. Create view in views.py
@"
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
"@ | Out-File -FilePath app\views.py -Encoding utf8

# 10. Include app URLs in project urls.py
$projectUrlsPath = "myproject\urls.py"
$includeLine = "    path('', include('app.urls')),"
(Get-Content $projectUrlsPath) -replace "from django.urls import path", "from django.urls import path, include" | Set-Content $projectUrlsPath
(Get-Content $projectUrlsPath) -replace "urlpatterns = \[", "urlpatterns = [`r`n$includeLine" | Set-Content $projectUrlsPath

# 11. Run development server
Write-Host "Starting server at http://127.0.0.1:8000/" -ForegroundColor Green
python manage.py runserver
'''