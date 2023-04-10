from django.urls import path
from .views import InstanceView, UserBasketView

app_name = "product"

urlpatterns = [
    path("instance/", InstanceView.as_view({'get': 'list'}), name='instance-list'),
    path("buy/", UserBasketView.as_view({'post': 'buy'}), name='buy-goods'),
]