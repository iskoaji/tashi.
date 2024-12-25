from django.shortcuts import render
from main.services import Services

def banner_list(request):
    banner = Services.services_func_id()
    return render(request, "index.html", locals())
