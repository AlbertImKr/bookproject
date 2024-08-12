from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    author = models.CharField(max_length=100, verbose_name='저자')
    publication_date = models.DateField(verbose_name='출판일')
    genre = models.CharField(max_length=100, verbose_name='장르')
    summary = models.TextField(verbose_name='요약')
    image = models.ImageField(upload_to='books/%Y%m%d', blank=True, null=True,
                              verbose_name='이미지')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '도서'
        verbose_name_plural = '도서들'
