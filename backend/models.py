from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    header = models.CharField("Заголовка", max_length=255)
    content = models.TextField()
    name = models.CharField("Имя", max_length=50)
    date = models.DateTimeField("Время", auto_now_add=True)
    category = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)
    img3 = models.CharField(max_length=255)

    def __str__(self):
        return self.header

class TopPost(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    name = models.CharField("Категория", max_length=255)
    count = models.IntegerField("Шт", default=1)

    def __str__(self):
        return self.name


class LatestPost(models.Model):
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    name = models.CharField("имя", max_length=255)
    date = models.DateTimeField("Время", auto_now_add=True)
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.name