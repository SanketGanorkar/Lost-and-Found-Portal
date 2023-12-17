from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    prn = models.CharField(max_length=8)
    branch = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=False)
    contact_number = models.CharField(max_length=20, unique=True, null=False)
    
    def __str__(self):
        return self.user.username
    
class Item(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    item_category = models.CharField(max_length=20)
    item_description = models.CharField(max_length=100, null=False)
    item_image = models.ImageField(null=False)
    location = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=False)
    verification_question = models.CharField(max_length=200, null=False)
    choice1 = models.CharField(max_length=100, null=False)
    choice2 = models.CharField(max_length=100, null=False)
    choice3 = models.CharField(max_length=100, null=False)
    choice4 = models.CharField(max_length=100, null=False)
    correct_choice = models.PositiveSmallIntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')], default=1)


class Notifications(models.Model):
    notification_choices = (
        ('Approved', 'Your claim was approved!'),
        ('Rejected', 'Your claim was Rejected!')
    )
    notification_type = models.CharField(max_length=100, choices=notification_choices)
    notification_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Claim(models.Model):
    claim_choices = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending')
    )
    claim = models.CharField(max_length=20, choices=claim_choices)

