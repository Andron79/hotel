from django.db import models

from admintools.models import CoreModel


class Category(CoreModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Категория номера'
    )

    class Meta:
        verbose_name = 'Категория номера'
        verbose_name_plural = 'Категории номеров'

    def __str__(self):
        return self.name


class Room(CoreModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        blank=False,
        verbose_name='Категория номера'
    )

    number = models.PositiveSmallIntegerField(
        verbose_name='№ Номера'
    )
    adults = models.PositiveSmallIntegerField(
        verbose_name='Взрослых',
        default=1
    )
    facilities = models.CharField(
        max_length=255,
        verbose_name='Оснащение номера',
    )
    size = models.PositiveSmallIntegerField(
        verbose_name='Площадь, м2',
    )
    bad_type = models.CharField(
        max_length=255,
        verbose_name='Тип кровати',
        default='Двух местная'
    )
    price = models.PositiveSmallIntegerField(
        verbose_name='Цена номера',
        default=0
    )
    description = models.TextField(
        max_length=2500,
        verbose_name='Описание номера'
    )

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Все номерa'

    def __str__(self):
        return f'№_{self.number}'

    def get_image(self):
        """ возвращает первую картинку среди дополнительных картинок товара """
        image = self.roomgallery_set.first()
        return image.image.url


class RoomGallery(CoreModel):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        verbose_name='Галерея фото',
    )
    image = models.ImageField(
        verbose_name='Фото номера',
        upload_to='rooms',
        blank=True,
    )

    sorting = models.PositiveSmallIntegerField(
        verbose_name='Сортировка фотографий',
        help_text='Сортировка по увеличению, начиная с 1. Фотография с наименьшим значением сортировки будет основной'
    )

    class Meta:
        ordering = ['sorting']
        verbose_name = 'Фотография номера'
        verbose_name_plural = 'Фотографии номеров'

    def __str__(self):
        return f'фото_{self.id}'

