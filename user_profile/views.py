from django.shortcuts import render

# Create your views here.
def user_profile(request):
    if request.user.is_authenticated():
        user_ = request.user
        context = {'user':user_,}
        return render(request, 'user_profile/user_profile.html', context)

    else:
        return render(request, 'home:home', {})
