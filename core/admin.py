from django.contrib import admin
from .models import User,Skills,Education,Experience,Works,SocialMedias,ContactMe
# Register your models here.
admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Education)
admin.site.register(Works)
admin.site.register(Experience)
admin.site.register(SocialMedias)
admin.site.register(ContactMe)

