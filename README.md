This is a live practice site that I am using to learn the ins and outs of `django-allauth`, a 3rd-party Django app for social authentication. Currently users can login with their Facebook account. Once logged in, users can also view their friends who have also logged in to the site.

I am interested in implementing a common feature on popular websites that allows a user to "find friends" through social accounts like Facebook and Twitter.

Doing this requires that `user_friends` is listed in the `SCOPE` of `facebook` listed under the `SOCIALACCOUNT_PROVIDERS` in `production.py` (the settings file).

It should be fairly trivial to return a queryset of the `User` or `UserProfile` objects so I can attach "add friend" buttons and show relevant information to the user about their friends in the context of my app. 
