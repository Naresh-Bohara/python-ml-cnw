from django.db import models

# Create your models here.
# model class is used to create database tables and define the structure of the data that will be stored in those tables. Each model class represents a table in the database, and each attribute of the model represents a field in that table. Models also provide methods for querying and manipulating the data in the database.

'''
class -> is used to define a model class in Django. The model class is a Python class that inherits from django.db.models.Model. This class represents a database table, and the attributes of the class represent the fields in that table.

field types -> are used to define the type of data that will be stored in each field of the model. Django provides various field types such as CharField for character fields, IntegerField for integer fields, DateTimeField for date and time fields, and many more. Each field type has its own set of parameters that can be used to customize the behavior of the field, such as max_length for CharField or default for any field type.

Meta class -> is an inner class that can be defined within a model class to provide additional metadata about the model. The Meta class can be used to specify options such as the database table name, ordering of records, verbose name for the model, and more. For example, you can use the Meta class to specify that the records should be ordered by a specific field or to set a custom name for the database table that will be created for the model.

field -> is an attribute of a model class that represents a specific piece of data that will be stored in the database. Each field is defined using a specific field type, such as CharField or IntegerField, and can have various parameters to customize its behavior. For example, you can define a CharField with a max_length parameter to specify the maximum number of characters allowed in that field. Fields are used to define the structure of the data that will be stored in the database and to provide validation for the data being entered.

objects -> is a default manager provided by Django for each model class. It is used to interact with the database and perform various operations such as querying, creating, updating, and deleting records. The objects manager provides methods like all(), filter(), get(), create(), and many more to facilitate these operations. For example, you can use MyModel.objects.all() to retrieve all records of a model or MyModel.objects.filter(name='John') to retrieve records that match a specific condition. The objects manager is an essential part of working with Django models and allows you to easily manipulate the data stored in the database.


syntax for defining a model class in Django:
from django.db import models
class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateTimeField()

    class Meta:
        db_table = 'my_model_table'
        ordering = ['field1']
        verbose_name = 'My Model'

    def __str__(self):
        return self.field1

model fields are defined as class attributes in the model class, and they represent the columns in the corresponding database table. Each field is an instance of a specific field type provided by Django, such as CharField, IntegerField, DateTimeField, etc. The field types determine the type of data that can be stored in that field and provide various parameters to customize their behavior. For example, a CharField can have a max_length parameter to specify the maximum number of characters allowed in that field, while an IntegerField can have a default parameter to specify a default value for that field. When you define a model class with its fields, Django will automatically create the corresponding database table with the appropriate columns based on the field definitions. You can then use the model to interact with the database, perform queries, and manipulate the data stored in those fields.

Model fields:
- CharField: Used for storing character data. It has a max_length parameter to specify the maximum number of characters allowed.
- IntegerField: Used for storing integer data. It can have a default parameter to specify a default value for the field.
- DateTimeField: Used for storing date and time data. It can have parameters like auto_now_add to automatically set the field to the current date and time when a new record is created, or auto_now to automatically update the field to the current date and time whenever the record is saved.


'''

'''
equivalent to the following SQL statement:
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    city VARCHAR(100),
    marks INTEGER
);
'''

class Students(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=18)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='students/', null=True, blank=True)
    marks = models.IntegerField()
    email  = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
