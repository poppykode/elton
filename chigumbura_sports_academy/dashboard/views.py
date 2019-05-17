from django.shortcuts import render

# Create your views here.
def dashboard_menu(request):
    template_name='dashboard/menu.html'
    return render(request,template_name)