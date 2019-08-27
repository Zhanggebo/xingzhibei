from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class AboutUs(View):
    def get(self, request):
        return render(request, 'about_us.html')




def page404(request):
    return render(request, '404.html', status=404)