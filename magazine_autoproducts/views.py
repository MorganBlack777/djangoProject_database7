from .models import Autoproduct
from .forms import AutoproductForm
from .filters import AutoproductFilter
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Store
from .forms import StoreForm
from .filters import StoreFilter

def get_url_for_pagination(request):
    url = str(request.get_full_path())
    if '?' in url:
        endpoint, args = url.split('?')
    else:
        endpoint, args = url, ''
    args = args.split('&')
    return F"{endpoint}?{'&'.join([i for i in args if 'page' not in i.split('=')[0]])}"

# Функция для отображения списка поставщиков с пагинацией
def store_list(request):
    # Получаем количество записей на странице из запроса, по умолчанию — 5
    records_per_page = int(request.GET.get('records_per_page', 5))

    store_filter = StoreFilter(request.GET, queryset=Store.objects.all())
    paginator = Paginator(store_filter.qs, records_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'store_list.html',
        {
            'page_obj': page_obj,
            'filter': store_filter,
            'own_url': request.path,  # Для пагинации
            'records_per_page': records_per_page,  # Для сохранения текущего выбора
            'admin': request.user.is_staff,  # Проверка на права администратора
        }
    )
# Функция для создания нового поставщика
def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    return render(request, 'store_form.html', {'form': form, 'action': 'Создать'})


# Функция для редактирования существующего поставщика
def store_edit(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store_list')
    else:
        form = StoreForm(instance=store)
    return render(request, 'store_form.html', {'form': form, 'action': 'Редактировать'})


# Функция для удаления поставщика
def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store_list')
    return render(request, 'store_confirm_delete.html', {'object': store})


#проверка, что запрос отправил админ
def is_admin(request) -> bool:
    if request.user.is_authenticated:
        if request.user.groups.filter(name='admin').exists():
            return True
        if request.user.is_superuser:
            return True
    return False

#обработчик для отображения главной страницы
def index(request):
    return render(
        request,
        'index.html',
        {
            "user": request.user if request.user.is_authenticated else None,
            "admin": is_admin(request)
        }
    )


# Функция для отображения списка автопродуктов с пагинацией
def autoproduct_list(request):
    # Получаем количество записей на странице из запроса, по умолчанию — 7
    records_per_page = int(request.GET.get('records_per_page', 7))

    autoproduct_filter = AutoproductFilter(request.GET, queryset=Autoproduct.objects.all())
    paginator = Paginator(autoproduct_filter.qs, records_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'autoproduct_list.html',
        {
            'page_obj': page_obj,
            'filter': autoproduct_filter,
            "own_url": get_url_for_pagination(request),  # Для пагинации
            'records_per_page': records_per_page,  # Для сохранения текущего выбора
            'admin': request.user.is_staff,  # Проверка на права администратора
        }
    )



    # Функция для создания новой записи
def autoproduct_create(request):
    if request.method == 'POST':
        form = AutoproductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('autoproduct_list')
    else:
        form = AutoproductForm()

    return render(request, 'autoproduct_form.html', {'form': form, 'action': 'Создать'})


# Функция для редактирования записи
def autoproduct_edit(request, pk):
    autoproduct = get_object_or_404(Autoproduct, pk=pk)
    if request.method == 'POST':
        form = AutoproductForm(request.POST, request.FILES, instance=autoproduct)
        if form.is_valid():
            form.save()
            return redirect('autoproduct_list')
    else:
        form = AutoproductForm(instance=autoproduct)

    return render(request, 'autoproduct_form.html', {'form': form, 'action': 'Редактировать'})


# Функция для удаления записи
def autoproduct_delete(request, pk):
    autoproduct = get_object_or_404(Autoproduct, pk=pk)
    if request.method == 'POST':
        autoproduct.delete()
        return redirect('autoproduct_list')

    return render(request, 'autoproduct_confirm_delete.html', {'object': autoproduct})

