from django.urls import path, include
from .views import UserListView, DeleteBookView
from . import views

urlpatterns = [
    path('accounts/login', views.UserLoginView.as_view(), name="login"),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('register/', views.UserCreateView.as_view(), name="register"),
    path('dashboard/', views.UserDashboardCreateView.as_view(), name="dashboard"),
    path('users/', views.UserDashboardDisplayUsers.as_view(), name="users"),
    path('delete/<int:pk>/', views.DeleteBookView.as_view(), name="book_delete"),
]
