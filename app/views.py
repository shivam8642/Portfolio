from django.shortcuts import render,redirect
from .models import MyDetail,Skill,Project,Contact
from .forms import ContactForm
from django.http.response import HttpResponseRedirect
# Create your views here.
def index(request):
    if request.method=="POST":
        data=ContactForm(request.POST)
        if data.is_valid():
            first_name=data.cleaned_data['first_name']
            last_name=data.cleaned_data['last_name']
            email=data.cleaned_data['email']
            message=data.cleaned_data['message']
            reg=Contact(first_name=first_name,last_name=last_name,email=email,message=message)
            reg.save()
            return redirect('/')
    else:
        data=ContactForm()
    obj=MyDetail.objects.all().values()
    skill=Skill.objects.all().values()
    project=Project.objects.all()
    return render(request,'index.html',{'obj':obj[0],'skill':skill,'pro':project,'data':data})