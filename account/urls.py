from django.urls import path
from django.contrib.auth import views as auth_views


from .views import user_login


app_name = 'account'

urlpatterns = [
	# path('login/', user_login, name='login'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]