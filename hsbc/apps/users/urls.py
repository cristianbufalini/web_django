from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(success_url = reverse_lazy('users:registro_completo')), name='registro'),
]