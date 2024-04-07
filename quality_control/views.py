from django.http import HttpResponse
from django.urls import reverse
from quality_control.models import BugReport, FeatureRequest

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')

    html = f'<h1>Система контроля качества</h1><a href="{bug_list_url}">Список всех багов</a><br/><a href="{feature_list_url}">Запросы на улучшение</a>'
    return HttpResponse(html)

def bug_list(request):
    bug_detail_url = reverse('quality_control:bug_list')
    html = '<h1>Список отчетов об ошибках</h1>'
    all_bugs = BugReport.objects.all()
    for bug in all_bugs:
        html += f'<a href="{bug_detail_url}{bug.id}/">Детали бага {bug.id}</a><br/>'
    return HttpResponse(html)


def feature_list(request):
    feature_detail_url = reverse('quality_control:feature_list')
    html = '<h1>Список запросов на улучшение</h1>'
    all_features = FeatureRequest.objects.all()
    for feature in all_features:
        html += f'<a href="{feature_detail_url}{feature.id}/">Детали бага {feature.id}</a><br/>'
    return HttpResponse(html)

def bug_detail(request, bug_id):
    return HttpResponse(f'Детали бага {bug_id}')

def feature_id_detail(request, feature_id):
    return HttpResponse(f'Детали улучшения {feature_id}')
