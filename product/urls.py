from django.urls import path
from .views import InstanceView

app_name = "product"

urlpatterns = [

    path("instance/", InstanceView.as_view({'get': 'list'}), name='instance-list'),
    # path('clothes/<int:pk>', SingleClothesView.as_view()),
    # path('clothes', ClothesView.as_view()),
    # path('price/<int:pk>', SinglePriceView.as_view()),
    # path('journal', RequestJournalView.as_view()),
]