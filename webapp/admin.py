from django.contrib import admin
from .models import House,Info,Picture,Message,Book,User

admin.site.register(Book)
admin.site.register(User)
admin.site.register(House)
admin.site.register(Info)
admin.site.register(Picture)
admin.site.register(Message)