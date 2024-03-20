
from django.urls import path
from .views import index,greeting,list_items,detail_item


urlpatterns = [
    path('facts/', index),
    path('greeting/', greeting),
    path('shop/', list_items, name = 'list_item'),
    path('shop/<int:item_id>/', detail_item, name = 'detail_item'),
]
