from django.shortcuts import render
from .models import Manga
import datetime
from django.views.generic import ListView
from django.db.models import Q
import calendar
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
        d_word = self.request.GET.get('day')
        m_word = self.request.GET.get('month')

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

        elif d_word:
            object_list = (Manga.objects.filter(Q(publish_date__day__gte=int(d_word))).
                filter(publish_date__month=monthnow).order_by('publish_date'))

        elif m_word:
            object_list = (Manga.objects.filter(Q(publish_date__month=int(m_word))).order_by('publish_date'))

        else:
            object_list = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')
        
        return object_list
    
    def get_context_data(self,**kwargs):
        day = [x for x in range(1,calendar.monthrange(dtnow.year,dtnow.month)[1]+1)]
        month = [monthnow-1,monthnow,monthnow+1]


        context = super().get_context_data(**kwargs)
        context['days'] = day
        context['months'] = month
    
        return context



    

    





