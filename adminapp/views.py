from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from authapp.models import User
from mainapp.models import ProductCategory, Product
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoriesAdminForm, ProductAdminForm


class IsSuperuserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


class UserListView(IsSuperuserMixin, ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'


class UserCreateView(IsSuperuserMixin, CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admin_staff:admin_users_read')


class UserUpdateView(IsSuperuserMixin, UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm


class UserDeleteView(IsSuperuserMixin, DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)


class CategoryListView(IsSuperuserMixin, ListView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-read.html'


class CategoryCreateView(IsSuperuserMixin, CreateView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-create.html'
    success_url = reverse_lazy('admin_staff:admin_categories_read')
    form_class = CategoriesAdminForm


class CategoryUpdateView(IsSuperuserMixin, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/admin-categories-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_categories_read')
    form_class = CategoriesAdminForm
    context_object_name = 'category'


@user_passes_test(lambda u: u.is_superuser)
def admin_categories_remove(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    category.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_categories_read'))


class ProductListView(IsSuperuserMixin, ListView):
    model = Product
    template_name = 'adminapp/admin-products-read.html'


class ProductCreateView(IsSuperuserMixin, CreateView):
    model = Product
    template_name = 'adminapp/admin-products-create.html'
    success_url = reverse_lazy('admin_staff:admin_products_read')
    form_class = ProductAdminForm


class ProductUpdateView(IsSuperuserMixin, UpdateView):
    model = Product
    template_name = 'adminapp/admin-products-update-delete.html'
    form_class = ProductAdminForm
    success_url = reverse_lazy('admin_staff:admin_products_read')
    context_object_name = 'product'


@user_passes_test(lambda u: u.is_superuser)
def admin_products_remove(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('admin_staff:admin_products_read'))
