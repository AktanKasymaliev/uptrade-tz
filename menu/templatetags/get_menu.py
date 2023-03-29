from django import template
from django.utils.html import format_html

from menu.models import Notes

register = template.Library()

@register.simple_tag
def draw_menu(menu_name: str) -> str:
    menu_items = get_menu_list(menu_name).select_related("parent")
    menu_html = "<ul>"
    for item in menu_items:
        menu_html += "<li>"
        if item.url:
            menu_html += format_html('<a href="{}/">{}</a>', item.url, item.title)
        else:
            menu_html += item.title
        menu_html += draw_children(item)
        menu_html += "</li>"
    menu_html += "</ul>"
    return format_html(menu_html)

def get_menu_list(menu_name: str) ->object:
    if menu_name and isinstance(menu_name, str):
        menu_items = Notes.objects.prefetch_related("children").filter(
            title__icontains=menu_name,
            parent__isnull=True
            )
    else:
        menu_items = Notes.objects.prefetch_related("children").filter(parent__isnull=True)
    return menu_items

def draw_children(item: object):
    if item.children.exists():
        children_html = "<ul>"
        parents = item.children.prefetch_related("children").all()
        for child in parents:
            children_html += "<li>"
            if child.url:
                children_html += format_html('<a href="{}/">{}</a>', child.url, child.title)
            else:
                children_html += child.title
            children_html += draw_children(child)
            children_html += "</li>"
        children_html += "</ul>"
        return format_html(children_html)
    else:
        return ""
