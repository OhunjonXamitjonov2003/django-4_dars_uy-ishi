from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Kategoriya", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Maqola nomi")
    content = models.TextField(blank=True, null=True, verbose_name="Matni")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")
    updated = models.DateTimeField(auto_now=True, verbose_name="Tahrirlangan vaqti")
    published = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'
        ordering = ('-pk',)


