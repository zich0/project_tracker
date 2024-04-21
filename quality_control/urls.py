from django.urls import path, include
from quality_control import views

app_name = 'quality_control'

bugs_patterns = [
    # path('', views.bug_list, name='bug_list'),
    # path('<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('new/', views.create_bug_report, name='new_bug'),
    path('create/', views.BugReportCreateView.as_view(), name='new_bug'),
    path('', views.BugListView.as_view(), name='bug_list'),
    path('<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    # path('<int:bug_id>/update', views.update_bug_report, name='bug_update'),
    path('<int:bug_id>/update', views.BugReportUpdateView.as_view(), name='bug_update'),
    # path('<int:bug_id>/delete', views.delete_bug_report, name='delete_bug'),
    path('<int:bug_id>/delete', views.BugReportDeleteView.as_view(), name='delete_bug'),
]

features_patterns = [
    # path('', views.feature_list, name='feature_list'),
    # path('<int:feature_id>/', views.feature_detail, name='feature_id_detail'),
    # path('new/', views.create_feature_request, name='new_feature'),
    path('create/', views.FeatureRequestCreateView.as_view(), name='new_feature'),
    path('', views.FeatureListView.as_view(), name='feature_list'),
    path('<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_id_detail'),
    # path('<int:feature_id>/update', views.update_feature_request, name='feature_update'),
    path('<int:feature_id>/update', views.FeatureRequestUpdateView.as_view(), name='feature_update'),
    # path('<int:feature_id>/delete', views.delete_feature_request, name='delete_feature'),
    path('<int:feature_id>/delete', views.FeatureRequestDeleteView.as_view(), name='delete_feature'),
]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', include(bugs_patterns), name='bug_list'),
    path('features/', include(features_patterns), name='feature_list'),
]