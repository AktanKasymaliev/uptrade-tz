from django import template
from django.utils.safestring import mark_safe

from menu.models import Notes

register = template.Library()

def get_menu_list(menu_name: str) ->object:
    if menu_name and isinstance(menu_name, str):
        notes = Notes.objects.filter(
            title__icontains=menu_name,
            parent__isnull=True
            )
    else:
        notes = Notes.objects.filter(parent=None)
    return notes

@register.simple_tag
def draw_menu(menu_name=""):
    notes = get_menu_list(menu_name).prefetch_related("children")
    return recursive_menu(notes)


def recursive_menu(notes):
    menu = "<ul>"
    for item in notes:
        menu += f'<li><a href="{item.url}/">{item.title}</a>'
        children = item.children.all()
        if children:
            menu += recursive_menu(children)
        menu += "</li>"
    menu += "</ul>"
    return mark_safe(menu)