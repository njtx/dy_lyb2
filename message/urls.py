from django.conf.urls import url
from . import views

app_name = 'message'
urlpatterns = {
    url(r'^message/$', views.getmsg, name='msg')
}