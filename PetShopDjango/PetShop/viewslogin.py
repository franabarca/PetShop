from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)

    username = data['username']
    password = data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response("Usuario Inválido")
    #se valida la pass
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response("Contraseña incorrecta")

    #crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    #print(token.key)
    return Response(token.key)
