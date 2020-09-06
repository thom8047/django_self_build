# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:02:21 2020

@author: Kyle
"""

from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]