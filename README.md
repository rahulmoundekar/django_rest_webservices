# Django Rest Framework Integration :

 Django REST framework is a powerful and flexible toolkit for building Web APIs.

>Some reasons you might want to use REST framework:

* The Web browsable API is a huge usability win for your developers.
* Authentication policies including packages for OAuth1a and OAuth2.
* Serialization that supports both ORM and non-ORM data sources.
* Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
* Extensive documentation, and great community support.
* Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.
# Project Setup

  - Making the project as :
     ```
     mkdir django_rest_webservices
	     cd django_rest_webservices
    ```
  - Install Django and DjangoRestFramework:
    ```
    pip install django
    pip install djangorestframework
    ```
  - Make apps (for class based views)
    ```
    django-admin startapp orm_onetoone_rest_curd_app
    ```
 - Integrating Django Rest
    ```
    pip install djangorestframework
    ```
 - Add 'rest_framework' and both apps to settings.py as:
    ```
    INSTALLED_APPS = [
		...
		'rest_framework',
		'orm_onetoone_rest_curd_app',
	   ]
    ```
 - Make a model
     ```
     from django.db import models
           
     class Person(models.Model):
            name = models.CharField(max_length=45)
            mobile = models.CharField(max_length=45)
        
            def __unicode__(self):
                return self.name
        
            class Meta:
                db_table = "person"
     ``` 
 - Make a serializer
     ``` 
     from rest_framework import serializers
     from orm_onetoone_rest_curd_app.models import Person
    
     class PersonSerializer(serializers.ModelSerializer):
            class Meta:
                model = Person
                fields = '__all__'
    ``` 
 - Make a view
     ``` 
   from rest_framework import viewsets
   from orm_onetoone_rest_curd_app.models import Person
   from orm_onetoone_rest_curd_app.serializers import PersonSerializer
    
   class PersonView(viewsets.ModelViewSet):
            serializer_class = PersonSerializer
            queryset = Person.objects.all()
    ```
 - In order to run the it apply migrations to make tables in db against models and runserver to test:
      ```
	  python manage.py makemigrations
	  python manage.py migrate
	  python manage.py runserver
      ```
   - Add it into the demo/settings.py as:
	```	
	# Parser classes to help default ll be JSONParser only.
	REST_FRAMEWORK = {
		# Parser classes priority-wise for Swagger
		'DEFAULT_PARSER_CLASSES': [
			'rest_framework.parsers.FormParser',
			'rest_framework.parsers.MultiPartParser',
			'rest_framework.parsers.JSONParser',
		],
		'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
	}	  

 - python manage.py runserver
    * Your swagger should run at: http://127.0.0.1:8000/swagger/	 
