from django.urls import path, reverse, reverse_lazy
from django.conf.urls import url
from . import views
from django.contrib.auth.views import(
										LoginView,
										LogoutView,
										PasswordResetView,
										PasswordResetDoneView,
										PasswordResetConfirmView,
										PasswordResetCompleteView,
									)

app_name = "accounts"

urlpatterns = [
	path('', views.home,name='home'),
	path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
	path('register/', views.register,name='register'),
	path('profile/', views.view_profile,name='view_profile'),
	path('profile/edit', views.edit_profile, name='edit_profile'),
	path('change_password/', views.change_password, name='change_password'),
	path('reset_password', PasswordResetView.as_view(template_name='accounts/reset_password.html', email_template_name='accounts/password_reset_email.html',success_url = reverse_lazy('accounts:password_reset_done')), name='reset_password'),
	path('reset_password/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
	# path(r'reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html',success_url = reverse_lazy('accounts:password_reset_complete')),name='password_reset_confirm'),
	path('reset_password/complete/', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete')
]