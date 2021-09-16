from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from CustomForms.models import CustomForm
from CustomForms.serializers import CustomFormSerializer


class CustomFormViewSet(viewsets.ModelViewSet):
    queryset = CustomForm.objects.all()
    serializer_class = CustomFormSerializer

    def list(self, request):
        queryset = CustomForm.objects.all()
        serializer = CustomFormSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CustomForm.objects.all()
        form = get_object_or_404(queryset, pk=pk)
        serializer = CustomFormSerializer(form)
        return Response(serializer.data)
