from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^vizes/(?P<viz>[\w.@+-]+)', views.vizes, name='vizes'),
    url(r'^project_management/', views.project_management, name='project_management'),
    url(r'^response/(?P<val>\d+\.\d{2})', views.response, name='response'),
]
