from django.conf.urls import url
from logtask import views

urlpatterns = [
    url(r'^login',views.logIN),
    url(r'^logout',views.logOUT),
    url(r'^createuser',views.createUSER),
    url(r'^changepwd',views.changePWD),
    url(r'^index',views.index)
]