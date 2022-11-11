from django.shortcuts import render,HttpResponse
from django.views.generic import View,TemplateView
# Create your views here.

class classbaseview(View):
    def get(self,request):
        return HttpResponse("<h1> This is class base view..</h1>")

class classtemplate(TemplateView):
    template_name = "test/hellow.html"


class Displyinfo(TemplateView):
    template_name = "test/info.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["name"]="sudhir"
        context["surname"]="Bhosale"
        context["city"]="Pune"
        return context