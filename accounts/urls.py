from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register_attempt, name="register_attempt"),
    path('accounts/login/', views.login_attempt, name="login_attempt"),
    path('token', views.token_send, name="token_send"),
    path('success', views.success, name='success'),
    path('verify/<auth_token>', views.verify , name="verify"),
    path('error', views.error_page, name="error"),
    path('forgot/', views.forgot, name='forgot'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('logout/', views.logout_request, name='logout'),
    path('add/', views.add, name='add'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:id>', views.update, name='update'),
    path('delete/<str:id>', views.delete, name='delete'),
]
