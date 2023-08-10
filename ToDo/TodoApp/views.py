from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.views.generic.edit import FormMixin

from .models import Tasks
from .forms import *

@login_required(login_url='login')
def home(request):
    return redirect('not_completed')

class Not_Completed(LoginRequiredMixin, ListView):
    template_name = 'TodoApp/not_completed.html'
    model = Tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {"title": "Not Completed", "tasks": self.get_queryset(), 'header_select': 2}
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        tasks = Tasks.objects.filter(user=self.request.user.id, completed=0)
        return tasks


class Completed(LoginRequiredMixin, ListView):
    template_name = 'TodoApp/completed.html'
    model = Tasks

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {"title": "Completed", "tasks": self.get_queryset(), 'header_select': 1}
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        tasks = Tasks.objects.filter(user=self.request.user.id, completed=1)
        return tasks

@login_required(login_url='login')
def delete(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    if task.user.id == request.user.id:
        task.delete()
    return redirect('home')

@login_required(login_url='login')
def complete(request, task_id):
    task = Tasks.objects.get(pk=task_id)
    if task.user.id == request.user.id:
        task.completed = 1
        task.save()
    return redirect('home')


class AddTask(LoginRequiredMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'TodoApp/addtask.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {"title": "Add Task", 'header_select': 3}
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditTask(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = 'TodoApp/edit.html'
    form_class = Edit
    success_url = reverse_lazy('home')
    login_url = 'login'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        task = Tasks.objects.get(pk=self.kwargs['task_id'])
        if task.user.id == self.request.user.id:
            car_instance = task
            kwargs['instance'] = car_instance
            return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {"title": 'Edit task', 'header_select': 3}
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "TodoApp/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': "Login"}
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'TodoApp/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = {'title': "Register"}
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect("login")