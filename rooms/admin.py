from django.contrib import admin

from rooms.models import (
    Category,
    Room,
    RoomGallery,
)


class RoomGalleryInLine(admin.StackedInline):
    """ Фото номеров """
    model = RoomGallery
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """ Номера """

    list_display = (
        'number',
        'category',
        'size',
        'price',
        'bad_type',
        'facilities',
    )
    inlines = [
        RoomGalleryInLine,
    ]


admin.site.register(Category)
admin.site.register(RoomGallery)
