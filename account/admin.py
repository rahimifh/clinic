from django.contrib import admin
from .models import Access,Profile,AccessItem
# Register your models here.
class AccessItemInline(admin.TabularInline):
    model = AccessItem
    raw_id_fields = ['Profile']

@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name','PersonnelCode' ]
    #list_filter = ['Receptionist',]
    inlines = [AccessItemInline]
    search_fields = ['first_name', 'last_name']
@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['Service','code' ]
    #list_filter = ['Receptionist',]
    search_fields = ['Service',]
