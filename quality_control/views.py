from django.http import HttpResponse
from django.urls import reverse
from quality_control.models import BugReport, FeatureRequest
from django.views.generic import ListView, DetailView
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f'<h1>Система контроля качества</h1><a href="{bug_list_url}">Список всех багов</a><br/><a href="{feature_list_url}">Запросы на улучшение</a>'
        return HttpResponse(html)

def bug_list(request):
    bug_detail_url = reverse('quality_control:bug_list')
    html = '<h1>Список отчетов об ошибках</h1>'
    all_bugs = BugReport.objects.all()
    for bug in all_bugs:
        html += f'<li>Название: <a href="{bug_detail_url}{bug.id}/">{bug.title}</a></br>Статус: {bug.status}<br/>'
    html += '</ul>'
    return HttpResponse(html)

def feature_list(request):
    feature_detail_url = reverse('quality_control:feature_list')
    html = '<h1>Список запросов на улучшение</h1>'
    all_features = FeatureRequest.objects.all()
    for feature in all_features:
        html += f'<li>Название: <a href="{feature_detail_url}{feature.id}/">{feature.title}</a></br>Статус: {feature.status}<br/>'
    html += '</ul>'
    return HttpResponse(html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>{bug.description}</p>'
        response_html += f'</br>Статус: {bug.status}'
        response_html += f'</br>Приоритет: {bug.priority}'
        response_html += f'</br>Связанный проект: {bug.project}'
        response_html += f'</br>Связанная задача: {bug.task.name}'
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>{feature.description}</p>'
        response_html += f'</br>Статус: {feature.status}'
        response_html += f'</br>Приоритет: {feature.priority}'
        response_html += f'</br>Связанный проект: {feature.project}'
        response_html += f'</br>Связанная задача: {feature.task.name}'
        return HttpResponse(response_html)
