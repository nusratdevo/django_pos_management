from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from main.models.subcategory import SubCategory
from main.forms.subcategory_form import SubCategoryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubCategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'subcategory/subcategory.html'
    success_message = "SubCategory successfully created!"
    model = SubCategory
    form_class = SubCategoryForm
    success_url = '/subcategory/'

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        data=SubCategory.objects.all()
        context["subcategory"] = data
        context["savebtn"] = 'Add to Inventory'
        return context       



@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubCategoryListView(ListView):
    template_name = 'subcategory/subcategory.html'
    model = SubCategory
    form_class = SubCategoryForm
    context_object_name = 'subcategory'
    paginate_by = 10


class SubCategoryUpdateView(UpdateView):
    template_name = 'subcategory/subcategory_update.html'
    model = SubCategory
    form_class = SubCategoryForm
    success_url = '/subcategory/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubCategoryDeleteView(DeleteView):
    template_name = 'subcategory/subcategory_delete.html'
    model = SubCategory
    success_url = '/subcategory/'
