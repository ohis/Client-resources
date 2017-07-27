from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):
    def loginUser(self,post):
             user = User.objects.filter(email=post.get('email')).first()
             if user and bcrypt.checkpw(post.get('password').encode(), user.password.encode()):
                 return {'status' :True, 'user':user}
             else:
                 return {'status': False, 'message': 'invalid credentials'}

    def validateUser(self,post):
        is_valid = True
        errors = []
        if len(post.get('name')) == 0 or len(post.get('name')) < 3:
            is_valid = False
            print "got to length if eq to 0"
            print len(post.get('name'))
            errors.append('Name field cannot be blank or less than 3')
        if len(post.get('name')) < 3:
            errors.append('Name field cannot be blank or less than 3')
        if not re.search(r'\w+\@\w+\.\w+',post.get('email')):
            is_valid = False
            errors.append('You must provide a valid email address')
        if len(post.get('password')) == 0 or len(post.get('password')) < 8:
            is_valid = False
            errors.append('Password cannot be blank or less than 8')
        if post.get('password') != post.get('password_confirmation'):
            is_valid = False
            errors.append('Your passwords do not match')
        return (is_valid,errors)



class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
