from django.http import HttpResponse
from django.urls import reverse
from quality_control.urls import app_name as qc_name

def index(request):
    another_page_url = reverse('tasks:another_page')
    qc_url = reverse(f'{qc_name}:main')
    html = f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на другую страницу</a><br/>"
    html += f"<a href='{qc_url}'>Quality control</a>"
    return HttpResponse(html)

def another_page(request):
    return HttpResponse("Это другая страница приложения tasks.")

