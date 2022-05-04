from django.contrib import admin

from women.models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'photo', 'is_published')  # Поля, которые будут видны в админ-панели.
    list_display_links = ('id', 'title')  # Поля, на которые можно кликнуть и перейти на страницу их редактирования.
    search_fields = ('title', 'content')  # По каким полям можно произовдить поиск.
    list_editable = ('is_published',)  # Запятая, так как это кортеж, в котором один элемент. Поля, которые можно редактировать.
    list_filter = ('time_create', 'is_published')  # sidebar справа: поля, по которым можем фильтровать записи.
    prepopulated_fields = {'slug': ('title',)}  # Ключ - поле, которое является слагом(SlugField). Значение - поле, по значению в котором будет формироваться значение слагового поля(в админке).

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Women, WomenAdmin)  # Регистрируем модели в админ-панели.
admin.site.register(Category, CategoryAdmin)
