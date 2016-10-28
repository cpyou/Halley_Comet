from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'userregist/$', views.user_regist, name='user_regist'),
    url(r'login/$', views.user_login, name='user_login'),
    url(r'userlogout/$', views.user_logout, name='user_logout'),
    url(r"^(\w{8})/$", views.turn, name='turn'),
]
