# from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny  # Agrega AllowAny aquí
from rest_framework import status
from django.contrib.auth.models import User
from .models import Influencer
from .serializers import InfluencerSerializer
from .utils import get_instagram_bio
from rest_framework import viewsets


class InfluencerViewSet(viewsets.ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Influencer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        username = serializer.validated_data['instagram_username']
        cookies = {}  # Agregar cookies aquí para autenticación en Instagram

        bio = get_instagram_bio(username, self.request.user)
        if "Error" in bio or "Failed" in bio:
            bio = "Scraping failed or no description found"

        serializer.save(user=self.request.user, description=bio)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scrape_instagram_bio(_request, username):
    cookies = {}  # Agregar cookies de sesión aquí
    bio = get_instagram_bio(username, cookies)

    if "Error" in bio or "Failed" in bio:
        return Response({"error": "Could not fetch Instagram bio"}, status=400)

    return Response({"username": username, "bio": bio})


@api_view(['POST'])
@permission_classes([AllowAny])  # Permite que cualquiera pueda registrarse
def register_user(request):
    """
    Endpoint para registrar un nuevo usuario.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_instagram_session(request):
    sessionid = request.data.get('sessionid')
    if not sessionid:
        return Response({"error": "sessionid is required"}, status=status.HTTP_400_BAD_REQUEST)

    session, created = InstagramSession.objects.get_or_create(
        user=request.user)
    session.sessionid = sessionid
    session.save()

    return Response({"message": "Session ID saved successfully"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_detail(request):
    print(f"🔍 Usuario autenticado en Django: {request.user}")
    return Response({"username": request.user.username})
