from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from app.forms import TeacherForm,TeacherUpdateForm
from .models import Teacher
# Create your views here.
def Index(request):
        form = TeacherForm(label_suffix=' - ' ,initial={'hobby':'dancing,singing'})
        return render(request,'index.html',{'form':form})

class teacher_registration(View):
        def post(self,request):
                fm = TeacherForm(request.POST)
                if fm.is_valid():
                        name =fm.cleaned_data['name']
                        age =fm.cleaned_data['age']
                        dob =fm.cleaned_data['dob']
                        gender =fm.cleaned_data['gender']
                        hobby =fm.cleaned_data['hobby']
                        image =request.FILES['image']
                        data = Teacher(name=name,age=age,dob=dob,gender=gender,hobby=hobby,image=image)
                        data.save()
                        return redirect('/table/')
                
class Table(View):
        def get(self,request):
                data = Teacher.objects.all()
                return render(request,'table.html',{'data':data})
        
class Delete(View):
        def get(self,request,uid):
                Teacher(id=uid).delete()
                return redirect('/table/')
        
def update(request,uid):
        fm = TeacherUpdateForm(label_suffix=' * ' ,initial={'hobby':'dancing,singing'})
        return render(request,'update.html',{'form':fm,'uid':uid})

def teacher_update(request):
                fm = TeacherUpdateForm(request.POST)
                if fm.is_valid():
                        uid = request.POST['hide']
                        name =fm.cleaned_data['name']
                        age =fm.cleaned_data['age']
                        dob =fm.cleaned_data['dob']
                        gender =fm.cleaned_data['gender']
                        hobby =fm.cleaned_data['hobby']
                        Teacher.objects.filter(id=uid).update(name=name,age=age,dob=dob,gender=gender,hobby=hobby)
                        return redirect('/table/')