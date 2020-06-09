from django.urls import path
from test_web import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search', views.search_drug_img, name='search-img'),
    path('text', views.search_drug_name, name='search-name'),
    path('drug/<int:pk>', views.DrugDetailView.as_view(), name='drug-detail'),
]