from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def create_job(request):
    return render(request, 'create_job.html')

def detail_job(request):
    return render(request, 'detail_job.html')

def profile(request):
    return render(request, 'profile.html')

def admin_page(request):
    return render(request, 'admin_page.html')