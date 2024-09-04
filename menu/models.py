from django.db import models

class MenuItemManager(models.Manager):
    def get_menu_with_children(self, menu_name):
        # Загружаем все пункты меню в одном запросе
        all_items = self.filter(menu_name=menu_name).order_by('parent__id', 'id')
        
        # Создаем словарь для хранения иерархии меню
        menu_dict = {}
        for item in all_items:
            menu_dict.setdefault(item.parent_id, []).append(item)
        
        # Рекурсивно строим иерархию меню
        def build_menu(parent_id=None):
            menu_items = []
            for item in menu_dict.get(parent_id, []):
                menu_item = {
                    'item': item,
                    'children': build_menu(item.id)
                }
                menu_items.append(menu_item)
            return menu_items
        
        return build_menu()

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    named_url = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=50)

    objects = MenuItemManager()

    def __str__(self):
        return self.title