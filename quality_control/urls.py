from django.urls import path, include
from quality_control import views

app_name = 'quality_control'

bugs_patterns = [
    path('', views.bug_list, name='bug_list'),
    path('<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
]

features_patterns = [
    path('', views.feature_list, name='feature_list'),
    path('<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_id_detail')
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', include(bugs_patterns), name='bug_list'),
    path('features/', include(features_patterns), name='feature_list'),
]