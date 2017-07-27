from __future__ import unicode_literals
from django.core.validators import RegexValidator
from ..login_reg.models import User

from phonenumber_field.modelfields import PhoneNumberField
import re, bcrypt
from django.db import models

class ClientManager(models.Manager):
    def addClient(self,post):
        is_valid = True
        errors = []
        if len(post.get('name')) == 0 or len(post.get('name')) < 3:
            is_valid = False
            errors.append('business name  entry cannot be empty or less than 3 characters')
        if len(post.get('phone')) < 10 or len(post.get('phone')) > 15:
            is_valid = False
            errors.append('invalid phone number')
        if len(post.get('notes')) == 0:
                is_valid = False
                errors.append('notes field cannot be empty')
        if not re.search(r'\w+\@\w+\.\w+',post.get('email')):
               is_valid = False
               errors.append('You must provide a valid email address')
        return (is_valid,errors)

        #return True
class ProjectManager(models.Manager):
    def update(self,post):
        is_valid = True
        errors = []
        if len(post.get('notes')) == 0:
                is_valid = False
                errors.append('notes field cannot be empty')
        return (is_valid,errors)

    def addProject(self,post):
        is_valid = True
        errors = []
        if len(post.get('name')) == 0:
            is_valid = False
            errors.append('project name  entry cannot be empty')
        if len(post.get('name')) < 3:
            is_valid = False
            errors.append('project name cannot be less than 3')

        if len(post.get('notes')) == 0:
                is_valid = False
                errors.append('notes field cannot be empty')
        return (is_valid,errors)

        #return True
class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = PhoneNumberField()
    notes = models.TextField()
    new_user = models.ForeignKey(User,related_name="new_clients" ,default= 2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()
class Project(models.Model):
    name = models.CharField(max_length=255)
    project_notes = models.TextField()
    client = models.ForeignKey(Client,related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProjectManager()



# Create your models here.
