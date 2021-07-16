from django.shortcuts import render
from .models import Manga
import datetime
# Create your views here.

def book_list(request):
    # url = 'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404'  #バッチ処理
    # api_key = ' #batch.py参照 '
    # params = {
    #     'size':9,
    #     'sort':'-releaseDate',
        
    #     'formatVersion':2,
    #     'applicationId': api_key,
    #     'elements':'title,salesDate,author,publisherName,mediumImageUrl,isbn',
    # }
    
    # Manga.objects.all().delete()

    # mangas =[]
    # start = 0
    # end = 0
    # while True:
    #     if end > 110:    # 何ページapiを取得するか
    #         break
    #     for i in range(10+start,13+end):
    #         params['page'] = i
    #         results = requests.get(url,params=params).json()
    #         try:
    #             for i in range(len(results['Items'])):

    #                 for_dayformat = results['Items'][i]['salesDate']       # modelの型に合わせてstrから日付の型に直す
    #                 reform_day = (for_dayformat.replace('年','').replace('月','').replace('日','').
    #                 replace('頃','').replace('上旬','').replace('中旬','01').replace('下旬','01').
    #                 replace('以降','01'))
    #                 if len(reform_day) < 8: # 202107という値が出るためとりあえず01
    #                     reform_day += '01'
    #                 dt = datetime.datetime.strptime(reform_day,'%Y%m%d')
    #                 manga = Manga(title=results['Items'][i]['title'],
    #                     publish_date=dt,
    #                     publisher=results['Items'][i]['publisherName'],author=results['Items'][i]['author'],
    #                     img=results['Items'][i]['mediumImageUrl'],isbn=results['Items'][i]['isbn'],
    #                 )
    #                 mangas.append(manga)
    #         except KeyError:
    #             pass
            
    #             # mangas.append(results['Items'][i])
    #     time.sleep(1)
    #     start += 3
    #     end += 3
        
    # Manga.objects.bulk_create(mangas)

    dtnow = datetime.datetime.now()
    monthnow = dtnow.month
    
    mangaslist = Manga.objects.filter(publish_date__month=monthnow).order_by('publish_date')
    
    return render(request,'bookpage/book_list.html',{'mangaslist':mangaslist})



def mypage(request):
    return render(request,'bookpage/mypage.html',{})