from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, Order,Staff
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from django.db.models import  Sum
# Create your views here.



def staff(request):
    staff = Product.objects.all()
    product_c=staff.count()
    group=Product.objects.values('category').order_by('category').annotate(Sum('quantity'))
    product_sum = Product.objects.all().aggregate(Sum('quantity'))['quantity__sum'] or 0.00
    category=Product.objects.values("category").order_by('category').annotate(total=Sum('quantity'))
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': staff,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_c,
        'product_sum':  product_sum,
        'group': group,
        'category':category,
    }
    return render(request, 'dashboard/staff.html', context)
   
@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    group=Product.objects.values('category').order_by('category').annotate(Sum('quantity'))
    product_sum= Product.objects.all().aggregate(Sum('quantity'))['quantity__sum'] or 0.00
    category=Product.objects.values("category").order_by('category').annotate(total=Sum('quantity'))
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'group':group,
        'category':category,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
        'product_sum':product_sum,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def products(request):
    product = Product.objects.all()
    quantity=Product.objects.values('category').annotate(Sum('quantity'))
    product_c=product.count()
    product_sum = Product.objects.all().aggregate(Sum('quantity'))['quantity__sum'] or 0.00
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'quantity':quantity,
        'customer_count': customer_count,
        'product_count': product_c,
        'product_sum':  product_sum,
    }
    return render(request, 'dashboard/products.html', context)
    

"""@login_required(login_url='user-login')"""
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customers.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,

    }
    return render(request, 'dashboard/customers_detail.html', context)


"""@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])"""
def product_edit(request, pk):
    product = Product.objects.all()
    quantity=Product.objects.values('category').annotate(Sum('quantity'))
    product_c=product.count()
    product_sum = Product.objects.aggregate(Sum('quantity'))
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'product': product,
        'form': form,
        'quantity':quantity,
        'customer_count': customer_count,
        'product_count': product_c,
        'product_sum':  product_sum,
    }
    return render(request, 'dashboard/products_edit.html', context)


"""@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])"""

def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)


@login_required(login_url='user-login')
def order(request):
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer = Product.objects.aggregate(Sum('quantity'))
    customer_count = customer.count()
    customer_sum= Product.objects.all().aggregate(Sum('quantity'))['quantity__sum'] or 0.00
    product = Product.objects.all()
    product_count = product.count()

    context = {
        'order': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
        'customer_sum':customer_sum,

    }
    return render(request, 'dashboard/order.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def order_edit(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-order')
    else:
        form = OrderForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def order_delete(request, pk):
    item = Order.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-order')
    context = {
        'item': item
    }
    return render(request, 'dashboard/order_delete.html', context)

@login_required(login_url='user-login')
def order_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/order_detail.html', context)

