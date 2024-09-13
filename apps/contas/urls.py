from django.urls import path
from contas.views import timeout, login

urlpatterns = [
    path('login/', login, name='login'),
    path('timeout/', timeout, name='timeout'),
]
