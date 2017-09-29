from django.conf.urls import url, include
from django.contrib.auth import views as loginView
from simplemooc.accounts import views as accountsViews
#from simplemooc.accounts import views as accountsViews

urlpatterns = [
	url(r'^$', accountsViews.dashboard,
    	name='dashboard'),
    url(r'^entrar/$', loginView.login,
    {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', loginView.logout,
    {'next_page': 'core:home'}, name='logout'),
    url(r'^cadastre-se/$', accountsViews.register,
    	name='register'),
    url(r'^nova-senha/$', accountsViews.password_reset,
        name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$',
        accountsViews.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^editar/$', accountsViews.edit,
    	name='edit'),
    url(r'^editar-senha/$', accountsViews.edit_password,
    	name='edit_password'),
]