from django import template
from django.template.loader import render_to_string
from menu.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    
    # Получаем иерархию меню в одном запросе
    menu_items = MenuItem.objects.get_menu_with_children(menu_name)
    
    if not menu_items:
        return ''
    
    # Рекурсивно устанавливаем флаг активности для пунктов меню
    def set_active_items(menu_items, request):
        for item in menu_items:
            item['item'].is_active = request.path == item['item'].url or request.path == item['item'].named_url
            set_active_items(item['children'], request)
    
    set_active_items(menu_items, request)
    
    # Рендерим меню
    context['menu_items'] = menu_items
    return render_to_string('menu.html', context.flatten())