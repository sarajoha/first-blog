from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^views/', views.post_list, name='post_list'),
]
#se usa la funcion de path o la de url??
