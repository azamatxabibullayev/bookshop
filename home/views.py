from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


class GetTest(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_authenticated():
            return render(request, 'get_test.html')
        else:
            return redirect('users:login')


