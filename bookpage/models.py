from django.db import models
from django.db.models.fields import URLField
from django.utils import timezone

# Create your models here.


# class Manga(models.Model):
#     id = models.IntegerField(primary_key=True)
#     author = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     publisher = models.CharField(max_length=200)
#     tag = models.CharField(blank=True,null=True,max_length=20)


#     def __str__(self):
#         return self.title

# class Series(models.Model):
#     manga_id = models.ForeignKey(Manga,on_delete=models.PROTECT,related_name='manga_id')
#     name = models.CharField(max_length=200)
#     number = models.IntegerField(blank=True,)
#     published_date = models.DateField(blank=True, null=True)
#     url = models.URLField(blank=True, null=True)
#     img = models.URLField(blank=True, null=True)
#     isbn = models.TextField(max_length=200)

class Manga(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    publish_date = models.DateField(blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    img = models.URLField(blank=True,null=True)
    isbn = models.TextField(max_length=200,default="")



class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class Favorite(models.Model):
    isbn = models.ForeignKey(Manga,on_delete=models.PROTECT)
    user_id = models.ForeignKey(User,on_delete=models.PROTECT)