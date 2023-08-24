from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category, Topping, Wrapper, IceCream

admin.site.empty_value_display = 'Не задано'


class IceCreamInline(admin.StackedInline):
    model = IceCream
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )

# Создаём класс, в котором будем описывать настройки админки:
class IceCreamAdmin(admin.ModelAdmin):
    # В этом классе опишем все настройки, какие захотим.
    list_display = (  # Показывать
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (  # Возможность изменить
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',)  # Поиск по
    list_filter = ('category',)  # Фильтрация справа
    list_display_links = ('title',)  # Переход по ссылке
    filter_horizontal = ('toppings',)  # Связь многие ко многим (для удобства)

# Регистрируем новый класс:
# указываем, что для отображения админки модели IceCream
# вместо стандартного класса нужно нужно использовать класс IceCreamAdmin

admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
