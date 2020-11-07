# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 22:28:38 2020

@author: Hitesh
"""


from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("locs",views.locs,name="locs")
    
    ]