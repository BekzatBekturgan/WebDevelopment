from django.urls import path
from .views.views import company_list, company_detail, vacancies_by_company, vacancies_list, vacancies_top10, vacancy_detail
from rest_framework_jwt.views import obtain_jwt_token
from api.views.fbv import company_list, company_detail, vacancies_list, vacancy_detail, vacancies_top10, vacancies_by_company

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies', vacancies_by_company),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten', vacancies_top10),
]
