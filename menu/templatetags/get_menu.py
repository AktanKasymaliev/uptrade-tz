from django import template
from django.urls import reverse
from django.utils.html import format_html

from menu.models import Notes

register = template.Library()

@register.simple_tag
def draw_menu(menu_name):
    menu_items = Notes.objects.filter(parent__isnull=True)
    menu_html = "<ul>"
    for item in menu_items:
        menu_html += "<li>"
        if item.url:
            menu_html += format_html('<a href="{}">{}</a>', item.url, item.title)
        else:
            menu_html += item.title
        menu_html += draw_children(item)
        menu_html += "</li>"
    menu_html += "</ul>"
    return format_html(menu_html)

def draw_children(item):
    if item.children.exists():
        children_html = "<ul>"
        for child in item.children.all():
            children_html += "<li>"
            if child.url:
                children_html += format_html('<a href="{}">{}</a>', child.url, child.title)
            else:
                children_html += child.title
            children_html += draw_children(child)
            children_html += "</li>"
        children_html += "</ul>"
        return format_html(children_html)
    else:
        return ""
