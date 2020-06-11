from django.urls import path
from test_web import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search-img/', views.search_drug_img, name='search-img'),
    path('search-name/', views.search_drug_name, name='search-name'),
    path('about-service/', views.about_service, name='ppiyak_service'),
    path('drug/<int:pk>', views.drug_detail, name='drug-detail'),
]