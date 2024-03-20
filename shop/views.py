import requests
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Item,Purchase


def index(request):
    url_cat = 'https://catfact.ninja/fact'

    try:
        response_cat = requests.get(url_cat)
        response_cat.raise_for_status()  # Проверяем статус ответа

        data = response_cat.json()
        fact_text = data.get('fact', 'Failed to fetch cat fact')
        return JsonResponse({'fact': fact_text})
    except requests.RequestException as e:
        # Если возникает ошибка при запросе к API
        print('Ошибка при получении данных о фактах: ', e)
        return JsonResponse({'error': 'Failed to fetch cat fact'}, status=500)

def greeting(request):
    return HttpResponse('Добро пожаловать')

def list_items(request):
    items = Item.objects.all()
    return render(request, 'list_item.html',{"items":items})

def detail_item(request,item_id):
    item = get_object_or_404(Item,pk=item_id)
    purchases = Purchase.objects.filter(item=item)
    return render(request,'detail_item.html',{'item': item,'purchase':purchases})