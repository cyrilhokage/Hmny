from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Playlist, Track
from django.views import generic
from .forms import Login_form, SignupForm, Playlist_Form, Track_Form
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage



#The index view
def index(request):

	#if the user is authenticated
	if request.user.is_authenticated :
		try:
			playlist_list = Playlist.objects.filter(user=request.user.id)
		except Playlist.DoesNotExist:
			raise Http404("Playlist or User does not exist")

	
		template = 'Music/userIndex.html'
		context = {'playlist_list' : playlist_list}

		
	else:

		form = Login_form()

		template = 'registration/login.html'

		context = {'form':form}

	
	return render(request, template, context)




#Alternative user view
def user_view(request, user_id):

	try:
		playlist_list = Playlist.objects.filter(user=user_id)
	except Playlist.DoesNotExist:
		raise Http404("Playlist or User does not exist")

	#template = loader.get_template('Music/userIndex.html')
	template = 'Music/userIndex.html'
	context = {'playlist_list' : playlist_list}

	return render(request, template, context)



#The playlist view
def playlist_view(request, playlist_id):
	response = "Vous etes sur la page d'une playlist dont l'id est : %s ."

	try:
		track_list = Track.objects.filter(playlist=playlist_id)
	except Playlist.DoesNotExist:
		raise Http404("Playlist Does not exist")

	template = 'Music/playlist.html'
	context = {'track_list' : track_list}

	return render(request, template, context)



#The track view
def track_view(request, track_title):
	response = "Vous etes sur la page de la chanson  %s ."

	return HttpResponse(response % track_title)


	

#Sing Up View
def signup(request):

	template="registration/signup.html"
	activation_mail_template = "registration/acc_active_email.html"


	if request.method == 'POST':

		form = SignupForm(request.POST)

		if form.is_valid():

			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string( activation_mail_template, {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token':account_activation_token.make_token(user),
            })

			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )

			email.send()

			return HttpResponse('Please confirm your email address to complete the registration')

	else:
		form = SignupForm()


	context = {'form': form}

	return render(request, template, context)


# Activation view
def activate(request, uidb64, token):

	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		
		return redirect('Music:User_View', user.id )
		
	else:
		return HttpResponse('Activation link is invalid!')



# Add playlist view
def add_playlist_view(request):

	template="Music/playlist_edit.html"

	if request.method == 'POST':

		form = Playlist_Form(request.POST)

		if form.is_valid():

			playlist = form.save(commit=False)
			user = request.user 
			playlist.user = user 

			playlist.save()

			return redirect('Music:User_View', user.id )

	else:
		form = Playlist_Form()


	context = {'form':form}

	return render(request, template, context)


# Add track view
def add_track_view(request):

	template="Music/track_form.html"

	if request.method == 'POST':

		form = Track_Form(request.POST)

		if form.is_valid():

			track = form.save()
			user = request.user 

			track.save()

			return redirect('Music:User_View', user.id )

	else:

		form = Track_Form()


	context = {'form':form}

	return render(request, template, context)


