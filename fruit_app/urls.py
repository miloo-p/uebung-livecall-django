from django.urls import path
from .views import start_page_view, single_fruit_view, all_fruit_view

urlpatterns = [

    path('', start_page_view),
    path('fruits/', all_fruit_view),
    path('fruits/<int:fruit_id>/', single_fruit_view),
]
