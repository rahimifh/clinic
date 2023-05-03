from django.test import TestCase
from django.db.models import Q
# Create your tests here.
''''
def search_patient(keyword, query_set):
    q1 = query_set.filter(Q(p_name__icontains=keyword))
    q2 = query_set.filter(Q(last_name__icontains=keyword))
    q3 = query_set.filter(Q(NationalCode__icontains=keyword))
    return (q1 | q2 | q3).order_by('-id')
def filter_turns(from_date, to_date, query_set):
    q1 = query_set.filter(Q(date_time__gte=from_date))
    q2 = query_set.filter(Q(date_time__lte=to_date))
    return (q1 & q2).order_by('-id')
def search_turns(keyword, query_set):
    q1 = query_set.filter(Q(Patient_p_name_icontains=keyword))
    q2 = query_set.filter(Q(Patient_last_name_icontains=keyword))
    q3 = query_set.filter(Q(Patient_NationalCode_icontains=keyword))
    return (q1 | q2 | q3).order_by('-id')
def search_refer_to_surgery(keyword, query_set):
    q1 = query_set.filter(Q(Patient_p_name_icontains=keyword))
    q2 = query_set.filter(Q(Patient_last_name_icontains=keyword))
    q3 = query_set.filter(Q(Patient_NationalCode_icontains=keyword))
    q4 = query_set.filter(Q(name_icontains=keyword))
    q5 = query_set.filter(Q(name_Doc_icontains=keyword))
    return (q1 | q2 | q3 | q4 | q5).order_by('-id')
def filter_refer_to_surgery(from_date, to_date, query_set):
    q1 = query_set.filter(Q(date_time__gte=from_date))
    q2 = query_set.filter(Q(date_time__lte=to_date))
    return (q1 & q2).order_by('-id')
'''
