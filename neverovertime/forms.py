# -*- coding: utf-8 -*-

from django import forms


class ProjectForm(forms.Form):
    """
    forms for Project
    """
    name = forms.CharField(max_length=50)
    manager = forms.CharField(max_length=50)
    expected_finish_time = forms.DateTimeField()
    description = forms.CharField(max_length=1000)