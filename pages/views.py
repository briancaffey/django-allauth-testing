from django.shortcuts import render

# Create your views here.

from django.views.generic import View
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'pages/home.html', {})
