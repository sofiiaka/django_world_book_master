from django.contrib import admin
from django.urls import path, include
from catalog import views
#from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('admin/', admin.site.urls),

    path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path(r'^books/$', views.BookListView.as_view(), name='books'),
    path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
]
# Добавление URL-адреса для входа в систему
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += [
   path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
]

# Add URLConf for librarian to renew a book.
# urlpatterns += [
#     path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
# ]

