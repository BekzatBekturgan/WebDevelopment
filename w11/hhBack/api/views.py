from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company
from api.models import Vacancy

def companies_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]
    return JsonResponse(companies_json, safe=False)

def company_details(request, id):
    try:
        company = Company.objects.get(id = id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json())

def company_vacancies(request, id):
    try:
        c = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = Vacancy.objects.filter(company=c)
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)


def vacancy_details(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())


def top_vacancies_by_salary(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)
# Create your views here.
