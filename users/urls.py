from django.urls import path
from .views import BlacklistTokenView, CustomUserCreate 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

app_name = 'users'

urlpatterns = [
    path('login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('login/refresh/',TokenRefreshView.as_view(),name="token_refresh"),
    path('register/',CustomUserCreate.as_view(),name="create_user"),
    path('logout/blacklist/',BlacklistTokenView.as_view(),name="blacklist")
]
