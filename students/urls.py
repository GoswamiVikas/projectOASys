from django.urls import path, reverse, reverse_lazy
from django.conf.urls import url
from accounts import views as ac_views

app_name = "students"

urlpatterns = [
	path('', ac_views.home,name='home'),
]