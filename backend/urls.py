from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import InfluencerViewSet, scrape_instagram_bio
from .views import register_user
from .views import user_detail

router = DefaultRouter()
router.register(r'influencers', InfluencerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', register_user, name='register_user'),
    path('scrape/<str:username>/', scrape_instagram_bio,
         name='scrape_instagram_bio'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("user/", user_detail, name="user_detail"),

]
