from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

# local
from .models import Account
from .serializers import RegistrarionSerializer


# Create your views here.

# POST  - Criando um conta
class AccountRegistrationView(APIView):
    """ POST - Registra uma nova conta """
    # Qualquer um pode acessar 
    permission_classes = [AllowAny]

    # Criando usuário
    def post(self, request):
        serializer = RegistrarionSerializer(data = request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Registrado com sucesso.'
            data['email'] = account.email
            data['username'] = account.username
            token = Token.objects.get(user=account).key
            data['token'] = Token
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        ####
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
