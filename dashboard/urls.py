from django.urls import path, include

from .views import dashboard, create_job, detail_job, profile, admin_page, dashboard_employer,Update_Job

app_name = "dashboard"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('create_job/', create_job, name="create_job"),
    path('detail_job/', detail_job, name="detail_job"),
    path('profile/', profile, name="profile"),
    path('admin_page/', admin_page, name="admin_page"),
    path('dashboard_employer/', dashboard_employer, name="dashboard_employer"),
    path('Update_Job/', Update_Job, name="Update_Job"),
]
