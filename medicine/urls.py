from django.conf.urls import url
from . import views

urlpatterns = [
    #/medicine/
    url(r'^$',views.index, name='index'),

    #/medicine//712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),    
]
