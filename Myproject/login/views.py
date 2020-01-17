from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,HttpResponse
def loginpage(request):
    #return HttpResponse('Welcome to login page')
    return render(request,'login.html',{})
def verifypage(request):
    #return HttpResponse('Welcome to verify page')
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('pw')
        from .models import AccountModel as am
        try:
            am.objects.get(user=u)
            return HttpResponse('Login Success')
        except:
            a=am()
            a.user=u
            a.pwd=p
            a.save()
            return HttpResponse('User created')



