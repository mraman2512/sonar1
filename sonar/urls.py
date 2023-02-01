from django.urls import path
from . import views

urlpatterns = [
    # path('scan/<str:project_id>/', views.scan_code),
    path('report/<str:project_id>/', views.fetch_report),
]
