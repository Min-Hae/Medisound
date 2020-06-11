from django.urls import path
from test_web import views

urlpatterns = [
    path('', views.main, name='main'),
    path('search-img/', views.search_drug_img, name='image_search'),
    path('search-name/', views.search_drug_name, name='text_search'),
    path('about-service/', views.about_service, name='ppiyak_service'),
    path('drug/<int:pk>', views.DrugDetailView.as_view(), name='drug_detail'),
]