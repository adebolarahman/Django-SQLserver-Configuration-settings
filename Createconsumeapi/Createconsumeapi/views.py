from Createconsumeapi.serialization import Serializationclass
from Createconsumeapi.models import Empmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter

@api_view(['GET'])
def showemp(request):
    if request.method=='GET':
        results=Empmodel.objects.all()
        serialize=Serializationclass(results,many=True)
        filter_backends = (DjangoFilterBackend,SearchFilter)
        search_fields= ('SOURCE_ACCT')

        return Response(serialize.data)