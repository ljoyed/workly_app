from django.contrib import admin
from django.urls import path
from accounts.views import login_view, dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
