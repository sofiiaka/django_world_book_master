from django.urls import path
from .import views
#from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
