from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialToken

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
		tolken = SocialToken.objects.filter(account__user=request.user, account__provider='facebook').first()
		print(tolken)
		target	= requests.get("https://graph.facebook.com/v2.9/" + fb_uid + "/friends?access_token=" + str(tolken))
		target = target.json()
		context['target'] = target
	return render(request, 'pages/profile_view.html', context)
