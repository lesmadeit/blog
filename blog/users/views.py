from django.shortcuts import render
from django.views import View
from .forms import UserCreationForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render

    def post(self, request):
        pass
