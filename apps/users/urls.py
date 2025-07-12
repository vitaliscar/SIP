from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('<int:pk>/', views.user_detail, name='user_detail'),
    path('', views.user_list, name='user_list'),
]
