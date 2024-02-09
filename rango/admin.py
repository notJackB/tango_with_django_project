from django.contrib import admin
from rango.models import Category, Page
#get our models from the rango app imported here

#create a class that can model the admin site itself
#by importing the ModelAdmin module
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    

#register them into the admin page
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
#formats the page site to have the new list system implemented
#in the class above




