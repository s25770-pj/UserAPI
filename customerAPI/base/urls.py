from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('employee/<str:pk>/', views.employee, name="employee"),

    # path('unique_names/', views.get_unique_names_with_count, name="unique_names"),
    # path('name_occurrences/<str:name>/', views.name_occurrences, name="name_occurrences"),
    path('search_by_age/<str:start_date>/<str:end_date>/', views.search_employees_by_age, name="search_by_age"),
    path('search_by_age/<str:start_date>/<str:end_date>/<int:num_records>/', views.search_employees_by_age_limit, name="search_by_age")
]