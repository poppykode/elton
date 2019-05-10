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
from .serializers import DependentSerializer
from dependencies.models import Dependent

@csrf_exempt
@api_view(["POST"])
def add_dependent(request):
    if request.method =='POST':
        serializer = DependentSerializer(data=request.data)
        request.data['guardian'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["GET"])
def get_dependents(request):
    if request.method =='GET':
        qs = Dependent.objects.filter(guardian=request.user)
        serializer = DependentSerializer(qs, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(["DELETE"])
def delete_dependent(request,pk):
    if request.method == 'DELETE':
        try:
            qs = Dependent.objects.get(pk=pk)
            qs.delete()
            message={'success':'successfully deleted.'}
            return Response(message,status=HTTP_204_NO_CONTENT)
        except Dependent.DoesNotExist:
            message={'error':'user does not exist.'}
            return Response(message,status=HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(["PUT"])
def update_dependent(request,pk):
    if request.method == 'PUT':
        try:
            qs = Dependent.objects.get(pk=pk)
            serializer = DependentSerializer(qs,data=request.data)
            request.data['guardian'] = qs.guardian.id
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
        except Dependent.DoesNotExist:
            message={'error':'user does not exist.'}
            return Response(message,status=HTTP_404_NOT_FOUND)
        








