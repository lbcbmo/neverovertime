# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):

    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()

    start_time = models.DateTimeField()
    expected_finish_time = models.DateTimeField()
    actual_finish_time = models.DateTimeField()

    manager = models.ForeignKey(User)

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)

    class Meta:
        ordering = ['-created_time']
