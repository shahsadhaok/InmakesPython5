from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"index.html")
def operations(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res1 = x + y
    res2 = x - y
    res3 = x * y
    res4 = x / y
    return render(request,'result.html',{'add':res1,'sub':res2,'mul':res3,'div':res4})
#def subtraction(request):
    #return render(request,"result.html")
#def multiplication(request):
    #return render(request,'result.html')
#def division(request):
    #return render(request,"result.html")