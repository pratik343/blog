from django.contrib import admin

# Register your models here.
from .models import Posts

class PostAdmin(admin.ModelAdmin):
   list_display = ('id', 'heading' , 'is_published' , 'blogger' )
   list_display_links = ('id', 'heading')
   list_filter = ('blogger',)
   list_editable = ('is_published',)
    
admin.site.register(Posts, PostAdmin)