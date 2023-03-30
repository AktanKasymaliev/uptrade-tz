from django import template
from django.utils.safestring import mark_safe



from menu.models import Notes

register = template.Library()

def get_menu_list(menu_name: str) ->object:
    if menu_name and isinstance(menu_name, str):
        notes = Notes.objects.prefetch_related("children").filter(
            title__icontains=menu_name,
            parent__isnull=True
            )
    else:
        notes = Notes.objects.prefetch_related("children").filter(parent=None)
    return notes



@register.simple_tag
def draw_menu(menu_name=""):
    notes = get_menu_list(menu_name)
    menu = "<ul>"
    for item in notes:
        menu += f'<li><a href="{item.url}/">{item.title}</a>'
        children = item.children.all()
        if children:
            menu += "<ul>"
            for child in children:
                menu += f'<li><a href="{child.url}/">{child.title}</a></li>'
            menu += "</ul>"
        menu += "</li>"
    menu += "</ul>"
    return mark_safe(menu)