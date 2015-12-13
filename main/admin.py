from django.contrib import admin
from .models import Book,Category
# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ('book_name', 'time_buying', )
	# list_display = ('book_name', 'time_buying', 'category')
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
