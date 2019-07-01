from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_list, name='users'),
    path('books/', views.books_list, name='books'),

    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    # path('books/<int:pk>/issue', views.book_issue, name='book_issue'),
    path('register/', views.Reg_user, name='register_user'),

]
