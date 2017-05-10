from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
# Create your views here.
import requests
from django.views.generic import View
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'pages/home.html', {})

def profile_view(request):
	fb_uid = SocialAccount.objects.filter(user_id=request.user.id, provider='facebook')
	fb_uid = fb_uid[0].uid
	context = {}
	if request.user.is_authenticated():

		 target	= requests.get("https://graph.facebook.com/v2.9/" + fb_uid + "/friends?access_token=EAACaPmdoqowBAHa63DkZCDPFD8G0JZC0sA0ZBUoQB2Bi0f8mj3MX3lj30Y9Sie5Bk1oKE0wzMFgoFdXVr1h2NrCfoqYMzmZCsdXwDiJcQXinARafpwFuRiDsszyFDvdlPbCD5kqIPZB92RY01GBFWOSxnUv4fwlRNjccj4WBCyypcyQxuEJ8d")
		 target = target.json()
		 context['target'] = target
	return render(request, 'pages/profile_view.html', context)
