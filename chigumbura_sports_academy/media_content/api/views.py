from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_204_NO_CONTENT,
    HTTP_201_CREATED
)
from rest_framework.response import Response
from .serializers import SportsCategorySerializer
from media_content.models import SportsCategory

@csrf_exempt
@api_view(["GET"])
@permission_classes((AllowAny,))
def get_sports_categories(request):
    if request.method =='GET':
        qs = SportsCategory.objects.all()
        serializer = SportsCategorySerializer(qs, many=True)
        return Response(serializer.data)