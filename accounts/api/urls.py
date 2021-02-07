  
from django.urls import path
from accounts.api.views import(
	registration_view,
	login_view, 
	# logout_view,

)
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
    path('login', login_view, name="login"),
	# path('logout', logout_view, name="logout"),
]