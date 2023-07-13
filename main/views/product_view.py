
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView, UpdateView
)

from main.forms.product_form import (
    ProductForm, VariantFormSet, ImageFormSet
)
from main.models.product import (
    Image, Product, Variant
)


class ProductInline():
    form_class = ProductForm
    model = Product
    template_name = "product/product_create.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.save()
        return redirect('list_products')

    def formset_variants_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        variants = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for variant in variants:
            variant.product = self.object
            variant.save()

    def formset_images_valid(self, formset):
        """
        Hook for custom formset saving. Useful if you have multiple formsets
        """
        images = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for image in images:
            image.product = self.object
            image.save()
            

@method_decorator(login_required(login_url='/login/'), name='dispatch')

class ProductCreate(ProductInline, CreateView):
    success_message = "Product successfully created!"

    def get_context_data(self, **kwargs):
        ctx = super(ProductCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx


    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'variants': VariantFormSet(prefix='variants'),
                'images': ImageFormSet(prefix='images'),
            }
        else:
            return {
                'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, prefix='variants'),
                'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, prefix='images'),
            }

class ProductUpdate(ProductInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(ProductUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'variants': VariantFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='variants'),
            'images': ImageFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='images'),
        }
    
@method_decorator(login_required(login_url='/login/'), name='dispatch')

class ProductList(ListView):
    model = Product
    template_name = "product/product.html"
    context_object_name = "products"
    

@login_required(login_url='/login/')

def delete_image(request, pk):
    try:
        image = Image.objects.get(id=pk)
    except Image.DoesNotExist:
        messages.success(request, 'Object Does not exit')
        return redirect('update_product', pk=image.product.id)

    image.delete()
    messages.success(request, 'Image deleted successfully')
    return redirect('update_product', pk=image.product.id)

@login_required(login_url='/login/')
def delete_variant(request, pk):
    try:
        variant = Variant.objects.get(id=pk)
    except Variant.DoesNotExist:
        messages.success(request, 'Object Does not exit')
        return redirect('update_product', pk=variant.product.id)

    variant.delete()
    messages.success(request, 'Variant deleted successfully')
    return redirect('update_product', pk=variant.product.id)



# @login_required(login_url='/login/')
# def product_list(request):
#     # data=Category.objects.all()
#     # form = CategoryForm()
#     # context={
#     #     'form':form,
#     #     'category':data,
#     # }
#     return render(request, "product/product.html")

# @login_required(login_url='/login/')
# def product_form(request):
#     # data=Category.objects.all()
#     # form = CategoryForm()
#     # context={
#     #     'form':form,
#     #     'category':data,
#     # }
#     return render(request, "product/product_create.html")
@login_required(login_url='/login/')
def product_stock(request):
    data=Product.objects.all()
    if request.method=="POST":
        query = request.POST.get('selector')
        if query == 'atoz' :
           atoz = query
           print(atoz)
        elif query == 'ztoa' :
           ztoa = query
           print(ztoa)
        elif query == 'hightolow' :
           hightolow = query
           print(hightolow)

        elif query == 'lowtohigh' :
           lowtohigh = query
           print(lowtohigh)
        elif query == 'newtold' :
           newtold = query
           print(newtold)
        else: 
          pass
    context={
        'products':data,
    }
    return render(request, "product/product_stock.html", context)

@login_required(login_url='/login/')
def update_qty(request, id):
    data = Product.objects.filter(id=id).first()
    # name = data[0]
    print('name', data)
    stock = Variant.objects.filter(product=id)
    context={
        'stock':stock,
        'data':data
    }
    return render(request, "product/stock_update.html", context)


def edit_qty(request):
   
        qty_id = request.POST.get('qty_id')
        # prod_id = request.POST.get('prod_id')
        qty = request.POST.get('qty_name')
        print('qty_id', qty_id, qty )
        try:
            variant = Variant.objects.get(id=qty_id)
            variant.quantity = qty
            variant.save()

            messages.success(request, "Quantity Updated Successfully.")
            return redirect('/stock/')

        except:
            messages.error(request, "Failed to Update.")
            return redirect('/stock/')