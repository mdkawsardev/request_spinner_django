from django.urls import path
from . import views
urlpatterns = [
    # path('', views.index, name='home'),
    path('', views.your_view_name, name='your_view_name'),
]
