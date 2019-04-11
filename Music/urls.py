from django.urls import path
from django.conf.urls import include, url
from django.views.generic.base import TemplateView

from . import views as views

from django.contrib.auth import views as Views




app_name = 'Music'
urlpatterns = [ 
	
		####	Authentification URLS
	
	#Th index page
	path('', views.index, name='index'), #ex: /Music/

	#To login
	path('login/', Views.LoginView.as_view(), name='login'),  #ex: /Music/login/

	#To logout
	path('logout/', Views.LogoutView.as_view(), name='logout'),  #ex: /Music/logout/	

	#To reset password
	path('password-reset/', Views.PasswordResetView.as_view(), name='password_reset'),
	path('password-reset/done/', Views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', Views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),	
	path('reset/done/', Views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

	#To change passwords
	path('password-change/', Views.PasswordChangeView.as_view(), name='password_change'),
	path('password-change/done/', Views.PasswordChangeDoneView.as_view(), name='password_change_done'),

	#to handle sign up with confirmation
	path('signup/', views.signup, name='signup'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),

	
		####	Other URLS
	
	#User index
	path('<int:user_id>/', views.user_view, name="User_View"),	#ex: /Music/5

	#To display user playlist
	path('playlist/<int:playlist_id>/', views.playlist_view, name='playlist'),	#ex: /Music/playlist/9

	#To display a playlist's songs
	path('track/<str:track_title>/', views.track_view, name='track'), #ex: /polls/track/8

	#To add a playlist
	path('playlist/add/', views.add_playlist_view, name='playlist_add'),  #ex: /playlist/add

	#To add a playlist
	path('playlist/track/add/', views.add_track_view, name='track_add'),  #ex: /playlist/track/add

	
]


	