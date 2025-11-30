from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Chef, Testimonial, ContactMessage


@admin.register(Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'photo_preview', 'featured')
    search_fields = ('name', 'role')
    list_filter = ('featured',)
    ordering = ('name',)
    readonly_fields = ('photo_preview_large',)

    fieldsets = (
        ('Chef Information', {
            'fields': ('name', 'role', 'bio', 'featured')
        }),
        ('Photo', {
            'fields': ('photo', 'photo_preview_large')
        }),
    )

    def photo_preview(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="height:50px; border-radius:5px;" />')
        return "No Image"

    def photo_preview_large(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" style="height:200px; border-radius:10px;" />')
        return "No Image"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'approved')
    list_filter = ('approved', 'rating')
    search_fields = ('name', 'role', 'message')
    ordering = ('name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'created_at', 'is_read')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at', 'is_read')
    readonly_fields = ('name', 'email', 'message', 'created_at')
    ordering = ('-created_at',)
    actions = ['mark_as_read', 'mark_as_unread']

    def has_add_permission(self, request):
        return False

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = "Message Preview"

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.order_by('-created_at')
