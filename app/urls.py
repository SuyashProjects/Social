from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', views.reg, name='reg'),
    url(r'^login/$', auth_views.login, {'template_name': 'app/login.html'}),
    url(r'^logout/$', auth_views.logout,{'template_name': 'app/logout.html'}, name='logout'),
    url(r'^$', views.main, name='main'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    url(r'^ajax/validate_password/$', views.validate_password, name='validate_password'),
]
