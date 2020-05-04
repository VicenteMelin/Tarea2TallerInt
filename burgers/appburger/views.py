from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from appburger.models import Ingrediente,Hamburguesa
from appburger.serializers import HamburguesaSerializer, IngredienteSerializer

@api_view(['GET', 'POST'])
def hamburguesa_list(request):


    if request.method == 'GET':
        burger = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(burger, many=True, context={'request': request})
        for x in serializer.data:
            for y in range(len(x['ingredientes'])):
                x['ingredientes'][y] = {'path': x['ingredientes'][y]}

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = HamburguesaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def hamburguesa_detail(request, pk):

    try:
        pk = int(pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        burger = Hamburguesa.objects.get(pk=pk)
    except Hamburguesa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HamburguesaSerializer(burger,context={'request': request})
        x = serializer.data
        for y in range(len(x['ingredientes'])):
            x['ingredientes'][y] = {'path': x['ingredientes'][y]}
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = HamburguesaSerializer(burger, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        burger.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def ingrediente_list(request):

    if request.method == 'GET':
        ingrediente = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingrediente, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def ingrediente_detail(request, pk):

    try:
        pk = int(pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data, status=status.HTTP_200_OK)


    elif request.method == 'DELETE':
        burger = Hamburguesa.objects.all()
        serializer = HamburguesaSerializer(burger, many=True, context={'request': request})
        for hb in serializer.data:
            for ing in hb['ingredientes']:
                if int(ing[-1]) == pk:
                    return Response(status=status.HTTP_409_CONFLICT)
        ingrediente.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
def delete_ingrediente(request, pkh, pki):

    try:
        pkh = int(pkh)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    try:
        pki = int(pki)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    try:
        ingrediente = Ingrediente.objects.get(pk=pki)
        hamburguesa = Hamburguesa.objects.get(pk=pkh)
    except Hamburguesa.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    except Ingrediente.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        hamburguesa.ingredientes.add(ingrediente)
        return Response(status=status.HTTP_201_CREATED)


    elif request.method == 'DELETE':
        hamburguesa.ingredientes.remove(ingrediente)
        return Response(status=status.HTTP_200_OK)