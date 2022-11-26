from django.urls import path

from pybo import views

app_name = 'pybo'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/<int:id>/', views.login_detail, name='login-detail')
]
