from django.db import models

STATUSES = [
    ('в наличии', 'В наличии'),
    ('под заказ', 'Под заказ'),
    ('ожидается поступление', 'Ожидается поступление'),
    ('нет в наличии', 'Нет в наличии'),
    ('не производится', 'Не производится')
]


class Item(models.Model):
    name = models.CharField(
        max_length=150, verbose_name='Название товара'
    )
    vendor_code = models.CharField(
        max_length=150, unique=True, verbose_name='Артикул товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена товара'
    )
    status = models.CharField(
        choices=STATUSES, max_length=150, verbose_name='Статус товара'
    )
    image = models.ImageField(
        upload_to='images/product/', verbose_name='Изображение товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
