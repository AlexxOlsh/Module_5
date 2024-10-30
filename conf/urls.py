from django.contrib import admin
from django.urls import path, include
from user.github_oauth_signup import GitHubOAuth2SignUpView
from user.github_oauth_signup_callback import GitHubOAuth2SignUpCallbackView
from user.github_oauth_login import GitHubOAuth2LoginView
from user.github_oauth_login_callback import GitHubOAuth2LoginCallbackView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path("signup/github/", GitHubOAuth2SignUpView.as_view(), name="github_signup"),
    path(
        "github/callback/signup",
        GitHubOAuth2SignUpCallbackView.as_view(),
        name="github_signup_callback",
    ),
    path("login/github/", GitHubOAuth2LoginView.as_view(), name="github_login"),
    path(
        "github/callback/login/",
        GitHubOAuth2LoginCallbackView.as_view(),
        name="github_login_callback",
    ),
]
