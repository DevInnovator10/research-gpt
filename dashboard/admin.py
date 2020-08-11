from django.contrib import admin
from .models import ChatSession, ChatMessage

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'user__username')

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'role', 'content', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('content',)
