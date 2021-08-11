from django.shortcuts import render
from .models import Manga
import datetime
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.


dtnow = datetime.datetime.now()
monthnow = dtnow.month

class BookList(ListView):
    model = Manga
    template_name = 'bookpage/book_list.html'
    
    
    
    def get_queryset(self):
        queryset = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')
        q_word = self.request.GET.get('query')
        f_word = self.request.GET.getlist('filter')

        if q_word:
            object_list = Manga.objects.filter(
                Q(title__icontains=q_word) | Q(author__icontains=q_word) 
                | Q(publisher__icontains=q_word)).filter(publish_date__month=monthnow).order_by('publish_date')
        elif f_word:
            if len(f_word) == 1:
                object_list = (Manga.objects.filter(Q(publisher__icontains=f_word[0]))
                .filter(publish_date__month=monthnow).order_by('publish_date'))
            elif len(f_word) == 2:
                object_list = (Manga.objects.filter(
                    Q(publisher__icontains=f_word[0]) | Q(publisher__icontains=f_word[1]))
                .filter(publish_date__month=monthnow).order_by('publish_date'))
            elif len(f_word) == 3:
                object_list = (Manga.objects.filter(
                    Q(publisher__icontains=f_word[0]) | Q(publisher__icontains=f_word[1])
                     | Q(publisher__icontains=f_word[2]))
                .filter(publish_date__month=monthnow).order_by('publish_date'))
            elif len(f_word) == 4:
                object_list = (Manga.objects.filter(
                    Q(publisher__icontains=f_word[0]) | Q(publisher__icontains=f_word[1])
                     | Q(publisher__icontains=f_word[2]) | Q(publisher__icontains=f_word[3]))
                .filter(publish_date__month=monthnow).order_by('publish_date'))
            elif len(f_word) == 5:
                object_list = (Manga.objects.filter(
                    Q(publisher__icontains=f_word[0]) | Q(publisher__icontains=f_word[1])
                     | Q(publisher__icontains=f_word[2]) | Q(publisher__icontains=f_word[4])
                    | Q(publisher__icontains=f_word[5]))
                .filter(publish_date__month=monthnow).order_by('publish_date'))            

        else:
            object_list = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')

        return object_list
    

    





# def book_list(request):
    
#     dtnow = datetime.datetime.now()
#     monthnow = dtnow.month
    
#     mangaslist = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')
    
#     return render(request,'bookpage/book_list.html',{'mangaslist':mangaslist})





# class MypageList(ListView):
#     model = Manga
#     template_name = 'mypage.html'
    # def mypage(request):
    # return render(request,'bookpage/mypage.html',{});