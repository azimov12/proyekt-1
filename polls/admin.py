from django.contrib import admin
from .models import NewsModel
from .forms import NewsForm


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = ('tittle', 'body', 'status')
    search_fields = ('tittle',)


admin.site.register(NewsModel, NewsAdmin)