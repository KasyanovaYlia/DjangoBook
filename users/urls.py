
from django.urls import path
from users.views import login, reg, profile, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('reg/', reg, name='reg'),
    path('profile/', profile, name='profile'),
path('logout/', logout, name='logout'),
]
