from django.contrib import admin
from booking.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class EventUserAdmin(UserAdmin):
    list_display = ['username', 'phone_number', 'profile_image']


admin.site.register(EventUserModel, EventUserAdmin)
admin.site.register(EventBookingModel)