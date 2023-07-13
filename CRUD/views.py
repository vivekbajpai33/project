from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from student.models import user


def  add(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('useremail')
        address = request.POST.get('useraddress')
        bio = request.POST.get('userbio')
        degree = request.POST.get('userdegree')
        dp = request.FILES['userdp']
            
        data = user(name=name,email=email,address=address,bio = bio,degree=degree,dp=dp) 
        data.save() 
            
            
    return render(request,'index.html')


def home(request):
    our  = user.objects.all()
    di = {
        'date':our
    }
    
    return render(request,'index.html',di)
        

        

        
            
        



    
    