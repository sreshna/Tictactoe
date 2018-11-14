from django.conf.urls import url

from player.views import home

urlpatterns = [
    url(r'home$', home)

]