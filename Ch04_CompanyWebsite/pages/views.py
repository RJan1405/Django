from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def home_page(request):
    context = {
        "car_list": ["TATA", "Mahindra", "Toyota", "Honda", "Ford"],
        "greeting": "Thank you FOR visitING.",
    }
    return render(request, 'home.html', context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "000-000-0000"
        return context