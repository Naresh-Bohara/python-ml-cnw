'''
steps for new django project:
1. Create a new directory for your project
2. Navigate to the directory

3. Create a virtual environment using:
    -  `python -m venv env`

4. Activate the virtual environment using: 
    - `source env/bin/activate` (Linux/Mac) or `env\Scripts\activate` (Windows)

5. Install Django using:
    -  `pip install django`
    check the version of django using:
    - `django-admin --version`

6. Create a new Django project using:
    - `django-admin startproject projectname .`
    here the dot at the end is important as it tells django to create the project in the current directory instead of creating a new directory with the project name.
    after this command, you should see the following files and directories in your project directory:
    - manage.py
    - projectname/
        - __init__.py
        - settings.py
        - urls.py
        - wsgi.py

7. Navigate to the project directory
    - `cd projectname`

8. Run the development server
    - `python manage.py runserver`
    this will start the development server and you can access your project at http://127.0.0.1:8000/

9. To create a new app within your project, run the following command:
    - `python manage.py startapp appname`
    this will create a new directory called `appname` with the following files:
    - __init__.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py

10. register the app in the `settings.py` file of your project (project/settings.py) by adding it to the `INSTALLED_APPS` list:
    - `INSTALLED_APPS = [ ... 'appname', ... ]`


11. Create a new model in the `models.py` file of your app (appname/models.py) and run the following commands to create and apply migrations:
    - `python manage.py makemigrations`
    - `python manage.py migrate`

12. Register your model in the `admin.py` file of your app (appname/admin.py) to make it accessible in the admin panel:
    - from .models import ModelName
    - admin.site.register(ModelName)

13. Create a superuser to access the admin panel using:
    - `python manage.py createsuperuser`
    follow the prompts to create a superuser account (username, email, password).

14. create views and templates to display your data on the frontend. You can create views in the `views.py` file of your app and templates in a `templates` directory within your app.

15. create  URLs for your views in the `urls.py` file of your app 

16, include the app's URLs in the project's `urls.py` file to make them accessible from the browser.

17. create templates folder in your app and create html files for your views.

18. if your templates are in a separate folder, make sure to add the path to the `TEMPLATES` setting in your project's `settings.py` file.
    - `TEMPLATES = [ { ... 'DIRS': [BASE_DIR / 'templates'], ... } ]`

19. Start the development server again and access the admin panel at http://127.0.0.1:8000/admin/
    log in with the superuser credentials you created and you should see your model listed there. You can add, edit, and delete records from the admin panel.
    - `python manage.py runserver`

20. To send data from the backend to the frontend, you can create views that query your models and pass the data to templates. For example, you can create a view that retrieves all records from a model and renders them in a template:
    - from django.shortcuts import render
    - from .models import ModelName

    - def model_list(request):
        - models = ModelName.objects.all()
        - return render(request, 'model_list.html', {'models': models})

21. In the template (model_list.html), you can loop through the data and display it:
    - {% for model in models %}
        - <p>{{ model.field_name }}</p>
    - {% endfor %}

22. To create a REST API, you can use Django REST Framework. First, install it using:
    - `pip install djangorestframework`
    then add it to your `INSTALLED_APPS` in `settings.py`:
    - `INSTALLED_APPS = [ ... 'rest_framework', ... ]`
    Next, create a serializer for your model in a new file called `serializers.py` in your app:
    - from rest_framework import serializers
    - from .models import ModelName

    - class ModelNameSerializer(serializers.ModelSerializer):
        - class Meta:
            - model = ModelName
            - fields = '__all__'
    Then, create a viewset in your `views.py` file to handle API requests:
    - from rest_framework import viewsets
    - from .models import ModelName
    - from .serializers import ModelNameSerializer
    - class ModelNameViewSet(viewsets.ModelViewSet):
        - queryset = ModelName.objects.all()
        - serializer_class = ModelNameSerializer
    Finally, create a router in your app's `urls.py` file to route API requests to the viewset:
    - from rest_framework import routers
    - from .views import ModelNameViewSet
    - router = routers.DefaultRouter()
    - router.register(r'models', ModelNameViewSet)
    - urlpatterns = [
        - path('', include(router.urls)),
    ]

'''
