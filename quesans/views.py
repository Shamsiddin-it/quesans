from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import *
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = "home.html"

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "category_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category_subcategory"] = Subcategory.objects.filter(category = self.kwargs["pk"])
        return context
    
    context_object_name = "category"

class CategoryCreateView(CreateView):
    model = Category
    template_name = "category_create.html"
    fields = ['name']
    success_url = reverse_lazy("category_list")

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category_update.html"
    fields = ['name']
    success_url = reverse_lazy("category_list")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("category_list")

class SubcategoryListView(ListView):
    model = Subcategory
    template_name = "subcategory_list.html"
    context_object_name = "subcategories"

class SubcategoryDetailView(DetailView):
    model = Subcategory
    template_name = "subcategory_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sub_question"] = Question.objects.filter(category = self.kwargs["pk"])
        return context
    
    context_object_name = "subcategory"

class SubcategoryCreateView(CreateView):
    model = Subcategory
    template_name = "subcategory_create.html"
    fields = ['category', 'name']
    success_url = reverse_lazy("subcategory_list")

class SubcategoryUpdateView(UpdateView):
    model = Subcategory
    template_name = "subcategory_update.html"
    fields = ['category', 'name']
    success_url = reverse_lazy("subcategory_list")

class SubcategoryDeleteView(DeleteView):
    model = Subcategory
    template_name = "category_delete.html"
    success_url = reverse_lazy("subcategory_list")

class UserListView(ListView):
    model = User
    template_name = "user_list.html"
    context_object_name = "users"

class UserDetailView(DetailView):
    model = User
    template_name = "user_detail.html"
    context_object_name = "user"

class UserCreateView(CreateView):
    model = User
    template_name = "user_create.html"
    fields = ['first_name', 'last_name', 'username', 'image', 'phone']
    success_url = reverse_lazy("user_list")

class UserUpdateView(UpdateView):
    model = User
    template_name = "user_update.html"
    fields = ['first_name', 'last_name', 'username', 'image', 'phone']
    success_url = reverse_lazy("user_list")

class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")

class QuestionListView(ListView):
    model = Question
    template_name = "question_list.html"
    context_object_name = "questions"

class QuestionDetailView(DetailView):
    model = Question
    template_name = "question_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_answer"] = Answer.objects.filter(question = self.kwargs["pk"])
        return context
    
    context_object_name = "question"

class QuestionCreateView(CreateView):
    model = Question
    template_name = "question_create.html"
    fields = ['title', 'description', 'category', 'image', 'file', 'user']
    success_url = reverse_lazy("question_list")

class QuestionUpdateView(UpdateView):
    model = Question
    template_name = "question_update.html"
    fields = ['title', 'description', 'category', 'image', 'file', 'user']
    success_url = reverse_lazy("question_list")

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "question_delete.html"
    success_url = reverse_lazy("question_list")

class AnswerListView(ListView):
    model = Answer
    template_name = "answer_list.html"
    context_object_name = "answers"

class AnswerDetailView(DetailView):
    model = Answer
    template_name = "answer_detail.html"
    context_object_name = "answer"

class AnswerCreateView(CreateView):
    model = Answer
    template_name = "answer_create.html"
    fields = ['title', 'description', 'question', 'image', 'file', 'user']
    success_url = reverse_lazy("answer_list")

class AnswerUpdateView(UpdateView):
    model = Answer
    template_name = "answer_update.html"
    fields = ['title', 'description', 'question', 'image', 'file', 'user']
    success_url = reverse_lazy("answer_list")

class AnswerDeleteView(DeleteView):
    model = Answer
    template_name = "answer_delete.html"
    success_url = reverse_lazy("answer_list")



