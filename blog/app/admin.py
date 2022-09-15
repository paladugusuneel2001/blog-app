from django.contrib import admin
from .models import person
from .models import post
# Register your models here.
class personAdmin(admin.ModelAdmin):
    list_display = ('name','email','is_active','gender')
    search_fields = ('name','email')
    list_filter = ('gender',)


admin.site.register(post)
admin.site.register(person,personAdmin)

