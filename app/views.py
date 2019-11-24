from django.shortcuts import render
from django.urls import reverse
from app.models import Phones
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from statsmodels.compat import urlencode


def view_index(request):

    data = Phones.objects.all().order_by('id')[3:]
    template = 'index.html'
    context = {'phones': data}
    return render(request, template, context)


def view_smartphones(request):

    data = Phones.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(data, 3)

    page = paginator.page(page_num)
    new_data = page.object_list

    if page.has_next() == True:
        next_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num + 1})
    else:
        next_page_url = None

    if page.has_previous() == True:
        prev_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num - 1})
    else:
        prev_page_url = None

    template = 'smartphones.html'

    context = {'phones': new_data,
               'current_page': page,
               'prev_page_url': prev_page_url,
               'next_page_url': next_page_url,
               }
    return render(request, template, context)


def view_phone(request, slug):

    template = 'phone.html'
    phone = Phones.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)


def view_empty_section(request):

    template = 'empty_section.html'
    context = {}
    return render(request, template, context)


def view_cart(request):

    template = 'cart.html'
    context = {}
    return render(request, template, context)


def view_login(request):

    template = 'login.html'
    context = {}
    return render(request, template, context)
