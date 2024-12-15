from django.shortcuts import render

# Create your views here. 

def forest(request):
    return render(request,'forest.html') 

def animals(request):
    return render(request,'animals.html')
