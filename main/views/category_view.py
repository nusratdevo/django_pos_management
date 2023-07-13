from django.shortcuts import redirect, render
from django.views.generic import  DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from main.models.category import Category
from main.forms.category_form import CategoryForm

@login_required(login_url='/login/')
def category_list(request):
    data=Category.objects.all()
    form = CategoryForm()
    context={
        'form':form,
        'category':data,
    }
    return render(request, "category/category.html", context)


@login_required(login_url='/login/')

def category_form(request, id=0):
    data=Category.objects.all()

    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            data = Category.objects.get(pk=id)
            form = CategoryForm(instance=data)
        context={
        'form':form,
        'category':data,
    }
        return render(request, "category/category_update.html", context)
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            data = Category.objects.get(pk=id)
            form = CategoryForm(request.POST,instance= data)
        if form.is_valid():
            form.save()
        return redirect('/category/')


def employee_delete(request,id):
    employee = Category.objects.get(pk=id)
    employee.delete()
    return redirect('/category/')
    
