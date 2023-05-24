from django.db import models

from email.policy import default
from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

quastions = [
    {
        'title': f'Question {i}',
        'text': f'Text {i}'
    } for i in range(7)
]
