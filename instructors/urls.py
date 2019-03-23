from django.urls import path, reverse, reverse_lazy
from django.conf.urls import url
from accounts import views as ac_views
from instructors import views

app_name = "instructors"

urlpatterns = [
	path('', ac_views.home,name='home'),
	path('add_subject/', views.add_subject, name = 'add_subject'),
	path('my_subjects/', views.my_subjects, name = 'my_subjects'),
	path('give_asmt/', views.give_asmt, name = 'give_asmt'),
	path('view_asmts/', views.view_asmts, name = 'view_asmts'),
	url(r'^view_submissions/(?P<asmt_name>[\w|\s]+)/$', views.view_submissions, name = 'view_class_asmts'),
]




# urlpatterns += patterns('',
#     url(r'^places/(?P<name>\w+)/$', 'misc.views.home', name='places.view_place')
# )

# # views.py
# def home(request, name):
#     place = models.Place.objects.get(name__iexact=name)
#     # Do more stuff here

# url(r'^(?P<username>\w+)/reviews/', include('foo.urls.reviews')),