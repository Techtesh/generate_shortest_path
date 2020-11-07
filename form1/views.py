from django.shortcuts import render
from django.http import HttpResponse

from . import loc
from .path import pathfinder
from .tsp3 import travellingSalesmanProblem
# Create your views here.
def home(request):
    return render(request,"f2.html")
    #return HttpResponse("Hello World")

def locs(request):
    l1=request.GET["l1"]
    l2=request.GET["l2"]
    l3=request.GET["l3"]
    l4=request.GET["l4"]
    l5=request.GET["l5"]
    l6=request.GET["l6"]
    l7=request.GET["l7"]
    l8=request.GET["l8"]
    l9=request.GET["l9"]
    l10=request.GET["l10"]
    l=[]
    if len(l1)>1:
        l.append(l1)
    if len(l2)>1:
        l.append(l2)
    if len(l3)>1:
        l.append(l3)
    if len(l4)>1:
        l.append(l4)
    if len(l5)>1:
        l.append(l5)
    if len(l6)>1:
        l.append(l6)
    if len(l7)>1:
        l.append(l7)
    if len(l8)>1:
        l.append(l8)
    if len(l9)>1:
        l.append(l9)
    if len(l10)>1:
        l.append(l10)
    
    data=[]
    
    for index,city in enumerate(l):
        val=loc.location_finder(city)
        print(index,city,val)
        data.append([index,city,val])
    print(data)
    
    print(l)
    newdata2=pathfinder(data)
    """
    newdata2=[[0.0, 557.559,17.228,45.994],
          [557.559,0,540.366,512.649],
          [17.228,540.366,0.0,29.756],
          [5.994,512.649,29.756,0]]
    """
    op=travellingSalesmanProblem(newdata2)
    op=list(op)[::-1]
    op.append(0)
    op=op[-1:]+op[:-1]
    op.append(0)
    print(op)
    l2=[]
    for x in op:
        l2.append(l[x])
    print(l2)
    return render(request,"f3.html",{"res":l2})
    #return HttpResponse("Thanks for travelling")#,{"list":l})