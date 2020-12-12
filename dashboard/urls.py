from django.urls import path, include

from .views import dashboard, create_job, detail_job, profile, admin_page

app_name = "dashboard"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('create_job/', create_job, name="create_job"),
    path('detail_job/', detail_job, name="detail_job"),
    path('profile/', profile, name="profile"),
    path('admin_page/', admin_page, name="admin_page"),
]
