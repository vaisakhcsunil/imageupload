from django.shortcuts import render,redirect

# Create your views here.
# from django.http import HttpResponse
# from django.views import View
# from django.views.generic.edit import CreateView

# from . models import student
# class studentcreate(CreateView):
#     model=student
#     template_name='create.html'
#     fields=["name","phonenumber"]

# from django.views.generic.list import ListView
# from .models import student
 
# class studentList(ListView):
 
#     # specify the model for list view
#     model = student
#     template_name='list.html'



# from django.views.generic.detail import DetailView
 
# from .models import student
 
# class studentDetailView(DetailView):
#     # specify the model to use
#     model = student
#     template_name='detail.html'


# from django.views.generic.edit import UpdateView
 
# from .models import student
 
# class studentupdateView(UpdateView):
#     # specify the model to use
#     model = student
#     template_name='update.html'
#     fields=["name","phonenumber"]
#     success_url ="/"



# from django.views.generic.edit import DeleteView
# from .models import student
# class studentDeleteView(DeleteView):
	
# 	model = student
# 	template_name='delete.html'
# 	success_url ="/"

from.forms import imageform
def upload(request):
    if request.method=='POST':
        form=imageform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form=imageform()
        return render(request,'image.html',{'form':form})