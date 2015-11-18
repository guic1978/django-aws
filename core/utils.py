# -*- coding: utf-8 -*-
from django.forms import TextInput, Textarea, CheckboxInput, CheckboxSelectMultiple
from django.forms.widgets import Select
from django.contrib import admin
from django.db import models

class CustomAdmin(admin.ModelAdmin):
    save_on_top = True
    actions = None
    list_select_related = True
    formfield_overrides = {
        models.CharField: {'widget':  TextInput(attrs={'style':'width:70%;'})},
        models.URLField: {'widget':  TextInput(attrs={'style':'width:70%;'})},
        models.ForeignKey: {'widget': Select(attrs={'style':'width:70%;'})},
        models.TextField: {'widget': Textarea(attrs={'style':'text-align:justify;width:70%;'})},
        models.BooleanField: {'widget': CheckboxInput(attrs={'style':'margin-top: 4px;'})},
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }