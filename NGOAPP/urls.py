from django.urls import path
from . import views


urlpatterns = [
    path('access',views.access,name='access'),
    path('login',views.logins,name='logins'),
    path('create_account/ngo',views.create_account,name='create_account'),
    path('dashboard/ngo',views.dashboard,name='dashboard'),
    path('ngo/create_post',views.create_post,name='create_post'),
    path('dashboard/philanthropist',views.dashboard,name='dashboard'),
    path('create_account/philanthropist',views.create_account_ph,name='create_account'),
    
]
