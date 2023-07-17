from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from .models import Employee
from django.db.models import Count
from django.http import JsonResponse


def home(request):
    employees = Employee.objects.all()

    context = {
        'employees': employees
    }
    return render(request, 'base/home.html', context)


def employee(request, pk):
    user_entity = Employee.objects.get(id=pk)
    context = {
        'user_entity': user_entity
    }
    return render(request, 'base/home.html', context)


def get_unique_names_with_count(request):
    names_with_count = Employee.objects.values('name').annotate(name_count=Count('name'))

    return JsonResponse({'names_with_count': names_with_count})


def name_occurrences(request, name):
    occurrences = Employee.objects.filter(name=name).annotate(name_count=Count('name'))
    context = {
        'name': name,
        'occurrences': occurrences}
    return JsonResponse({'name': name, 'occurrences': occurrences})


def search_employees_by_age(request, start_date, end_date, num_records=None):
    if request.method == 'GET':
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()

        employees = Employee.objects.filter(birth_date__range=(start_date, end_date))

        if num_records:
            employees = employees[:num_records]

        employee_data = [
            {
                'id': employee.id,
                'name': employee.name,
                'surname': employee.surname,
                'birth_date': employee.birth_date.strftime('%Y-%m-%d'),
            }
            for employee in employees
        ]

        return JsonResponse({'employees': employee_data})


def search_employees_by_age_limit(request, start_date, end_date, num_records):
    return search_employees_by_age(request, start_date, end_date, num_records)
