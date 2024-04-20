from quality_control.models import BugReport, FeatureRequest
from tasks.models import Project, Task
from django.views.generic import ListView, DetailView
from django.views import View
from django.shortcuts import render, redirect
from .forms import BugReportForm, FeatureRequestForm
from django.shortcuts import get_object_or_404

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})

def create_bug_report(request):

    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bug = form.save()

            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            feature = form.save()

            return redirect('quality_control:feature_id_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})