from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('cadastro/',views.cadastro, name='cadastro'),
    path('app/homepage', views.homepage, name='homepage'),
    path('app/accountingManagement', views.accountingManagement, name='accountingManagement'),
    path('app/financialReport', views.financialReport, name='financialReport')
]

