from django.contrib import admin

# Register your models here.
from user_profile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'emoji', 'bio',)

    def emoji(self, obj):
        return obj.emoji

    def bio(self, obj):
        return obj.bio

admin.site.register(UserProfile, UserProfileAdmin)
