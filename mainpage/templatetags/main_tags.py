
from django import template
from django.shortcuts import render, get_object_or_404
register = template.Library()
from ..forms import Searchbox

@register.inclusion_tag('main/search.html')
def show_search ():
    return{'searchform':Searchbox}
