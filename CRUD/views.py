from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import redirect
from student.models import user
from django.template import loader




# addition and show data
def home(request):
    
    if request.method == 'POST':
        
        
        # fm = user(request.POST)
        
        studentname = request.POST.get('username')
        studentemail = request.POST.get('useremail')
        studentaddress = request.POST.get('useraddress')
        post = request.FILES.get('post')
        studentbio = request.POST.get('userbio')
        studentdegree = request.POST.get('userdegree')
        

        data = user(name=studentname,email=studentemail,address=studentaddress,bio=studentbio,degree=studentdegree,dp=post)
        data.save()
        
        fm = user.objects.all()
    else:
        fm = user.objects.all()      
  
    return render(request,'index.html',{'output':fm})


# update 

def update(request,id):
    if request.method == 'POST':
        di = user.objects.get(id = id)   
        di.name = request.POST.get('upname') 
        di.email = request.POST.get('upemail')
        di.address = request.POST.get('upaddress')
        di.bio = request.POST.get('upbio')
        di.degree = request.POST.get('degree')
        di.dp = request.FILES.get('post')
         
        di.save()
        
        fm = user.objects.all()
    else:
        fm = user.objects.all()           
             
    return render(request,'update.html',{'updata':fm})


# delete
def delet(request,id):
    if request.method == 'POST':
        de = user.objects.get(pk=id)
        de.delete()
        
    return HttpResponseRedirect('/')


        

        
            
        



    
    