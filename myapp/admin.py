from django.contrib import admin
from myapp import models
# Register your models here.


#to display the column names along with values, we should use below methods and we should import models.Modeladmin funtion

class TopicAdminView(admin.ModelAdmin):
    list_display=('topic_name',)    #displays the column names
    search_fields=('topic_name',)   #searches according to value given for the attribute search_fields


class WebpageAdminView(admin.ModelAdmin):
    list_display=('topic','name','url')
    search_field=('name',)
    list_editable=('name',)   #value (column name) given for the method can be modified.
    list_filter=('topic',)

class AccessDetailsAdminView(admin.ModelAdmin):
    list_display=('webpage','datetime')
    search_fields=('webpage','datetime')



admin.site.register(models.Topic,TopicAdminView)
admin.site.register(models.Webpage,WebpageAdminView)
admin.site.register(models.AccessDetails,AccessDetailsAdminView)    #Registering the models to access from admin side at backend(backend)

