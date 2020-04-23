from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
import json
from api.models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt


#CRUD and Serializer done
from api.serializers import CompanySerializer, VacancySerializer


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#CRUD and Serializer done
@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})

#GET and SERIALIZER
@csrf_exempt
def vacancies_by_company(request, company_id):
    try:
        companies = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        vacancies = companies.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
       # vacancies_json = [v.to_json() for v in vacancies]
        return JsonResponse(serializer.data, safe=False)

#CRUD AND SERIALIZER DONE
@csrf_exempt
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = VacancySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

#CRUD AND SERIALIZER DONE
def vacancy_detail(request, vacancy_id):
    try:
        vacancies = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = CompanySerializer(vacancies)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=vacancies, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})
    elif request.method == 'DELETE':
        vacancies.delete()
        return JsonResponse({'deleted': True})

#GET and SERIALIZER
def vacancies_top10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by("-salary")[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)


# Create your views here.
