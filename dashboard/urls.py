from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('chat/', views.chat_view, name='chat'),

    path('chat/<int:session_id>/', views.chat_view, name='chat_with_session'),
    path('chat/new/', views.new_chat_view, name='new_chat'),
    path('chat/send-message/', views.send_message, name='send_message'),
    path('chat/delete-session/', views.delete_chat_session, name='delete_chat'),
    path('chat/get-sessions/', views.get_session_list, name='get_session_list'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
