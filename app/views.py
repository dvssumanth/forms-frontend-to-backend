from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def i_scl(request):
    if request.method=='POST':
        scn=request.POST['scn']
        scl=request.POST['scl']
        so=School.objects.get_or_create(scname=scn,scloc=scl)[0]
        so.save()
        qsso=School.objects.all()
        d={'qsso':qsso}
        return render(request,'disp.html',d)
    return render(request,'i_scl.html')
def i_std(request):
     qsso=School.objects.all()
     d={'qsso':qsso}
     if request.method=='POST':
        stn=request.POST['stn']
        sti=request.POST['sti']
        scn=request.POST['scn']
        so=School.objects.get(scname=scn)
        st=Student.objects.get_or_create(scname=so,stdname=stn,stdid=sti)[0]
        st.save()
        qsto=Student.objects.all()
        d1={'qsto':qsto}
        return render(request,'disp1.html',d1)
     return render(request,'i_std.html',d)