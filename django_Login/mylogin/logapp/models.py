from django.db import models

class Logger(models.Model):
    first_name = models.CharField(max_length = 200)
    Last_name = models.CharField(max_length = 200)
    time_log = models.TimeField(help_text="Enter the exact time")