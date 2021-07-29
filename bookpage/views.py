from django.shortcuts import render
from .models import Manga
import datetime
from django.views.generic import ListView
# Create your views here.

class BookList(ListView):
    model = Manga
    template_name = 'bookpage/book_list.html'

    dtnow = datetime.datetime.now()
    monthnow = dtnow.month
    queryset = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')


    





# def book_list(request):
    
#     dtnow = datetime.datetime.now()
#     monthnow = dtnow.month
    
#     mangaslist = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')
    
#     return render(request,'bookpage/book_list.html',{'mangaslist':mangaslist})





class MypageList(ListView):
    model = Manga
    template_name = 'bookpage/mypage.html'
    # def mypage(request):
    # return render(request,'bookpage/mypage.html',{});