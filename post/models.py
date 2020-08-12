from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    #작가추가!
    author = models.CharField(max_length= 10,default= '')

    def __str__(self):
        return self.title #self.pub_date로 하면 날짜기준으로 보인다.

    def summary(self):
        return self.body[:10] #testfield는 배열이구나