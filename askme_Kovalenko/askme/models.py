from django.db import models

# Create your models here.

quastions = [
    {
        'title': f'Question {i}',
        'text': f'Text{i}'
    } for i in range(100)
]
