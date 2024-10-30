from django.shortcuts import redirect
from django.urls import reverse

from rest_framework.views import APIView
from user.utils import github_setup


class GitHubOAuth2SignUpView(APIView):
    def get(self, request):
        redirect_uri = request.build_absolute_uri(reverse("github_signup_callback"))
        return redirect(github_setup(redirect_uri))