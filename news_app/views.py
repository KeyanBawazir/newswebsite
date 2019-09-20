from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',{'title':'home'})
def sports(request):
    return render(request,'sports.html',{'title':'sports'})
def yemennews(request):
    return render(request,'yemennews.html',{'title':'yemenews'})    