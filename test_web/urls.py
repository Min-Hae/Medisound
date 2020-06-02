from django.urls import path
from test_web import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search', views.search_drug, name='search-drug'),
    path('text', views.text_detect, name='get-text'),
    path('drug/<int:pk>', views.DrugDetailView.as_view(), name='drug-detail'),
]