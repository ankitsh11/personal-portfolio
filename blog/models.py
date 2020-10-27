from django.db import models

class blog_model(models.Model):
    title=models.CharField(max_length=(100))
    description=models.CharField(max_length=(100))
    date=models.DateField()

    def __str__(self):
        return self.title
