from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from user.utils import github_callback


class GitHubOAuth2SignUpCallbackView(APIView):
    def get(self, request):

        User = get_user_model()
        redirect_uri = request.build_absolute_uri(reverse("github_signup_callback"))
        auth_uri = request.build_absolute_uri()

        user_data = github_callback(redirect_uri, auth_uri)

        user, _ = User.objects.get_or_create(username=user_data["login"],
                                             defaults={"github_id": user_data["id"]})

        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({"token": token.key})