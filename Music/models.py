from django.db import models
from django.contrib.auth.models import User



#Playlist model
class Playlist(models.Model):
	id = models.AutoField(primary_key=True) #Django gives each model this field by default
	title = models.CharField(max_length=200, help_text="Enter a name of your playlist")
	date_created = models.DateField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='playlist')
	
	def __str__(self):
		return self.title
		


#Track model		
class Track(models.Model):
	track_title = models.CharField(max_length=300)
	playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, null=True)
	stream_source = models.CharField(max_length=1000, help_text="copy and paste the URL link of the track")
	
	def __str__(self):
		return self.track_title
