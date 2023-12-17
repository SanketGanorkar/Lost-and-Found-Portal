from django.contrib import admin
from .models import Student, Item, Notifications, Claim

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_id', 'first_name', 'last_name', 'branch', 'email', 'contact_number']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['student', 'location', 'item_category', 'item_description', 'item_image']

@admin.register(Notifications)
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ['notification_type', 'notification_description', 'created_at']

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['claim']

