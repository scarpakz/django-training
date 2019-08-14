from django.shortcuts import render
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.urls import reverse_lazy
from .models import Book

from .forms import BookForm, SignUpForm

class UserListView(ListView):
    model = User

class UserLoginView(views.LoginView):
    template_name = 'account/login.html'
    
    def get_success_url(self):
        url = reverse_lazy('dashboard')
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

class UserCreateView(CreateView):
    template_name = 'account/register.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

@method_decorator(login_required, name='dispatch')
class UserDashboardCreateView(CreateView, ListView):
    model = Book
    template_name = 'account/dashboard.html'
    fields = ['name', 'description', 'author']
    success_url = reverse_lazy('dashboard')
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class UserDashboardDisplayUsers(ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'account/users.html'

class UserLogoutView(views.LogoutView):
    model = Book
    template_name = 'account/logout.html'

@method_decorator(login_required, name='dispatch')
class DeleteBookView(DeleteView):
    model = Book
    success_url = reverse_lazy('dashboard')

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    template_name = 'account/add_book.html'
    form_class = BookForm
    success_url = reverse_lazy('dashboard')

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    form_class = BookForm
    queryset = Book.objects.all()
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('dashboard')