from django.urls import path
from . import views

urlpatterns = [
    path('',views.BookList.as_view(),name='book_list'),
    # path('mypage/',views.MypageList.as_view(),name='mypage'),  
]