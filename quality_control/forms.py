from django import forms
from django.forms import ModelForm
from .models import BugReport, FeatureRequest
from tasks.models import Project, Task

class BugReportForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    task = forms.ModelChoiceField(queryset=Task.objects.all(), to_field_name='name')
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']


class FeatureRequestForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all())
    task = forms.ModelChoiceField(queryset=Task.objects.all(), to_field_name='name')
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']