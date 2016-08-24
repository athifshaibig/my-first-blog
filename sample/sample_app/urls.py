from django.conf.urls import url, static, patterns
from sample_app import views

urlpatterns = [

  url(r'^$', views.home, name='home'),

]


