from .serializers import TeamSerializer, PlayerSerializer, MatchesSerializer,  PointsSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse , JsonResponse , Http404
from rest_framework.decorators import api_view
from rest_framework.renderers import BrowsableAPIRenderer
from .models  import Team , Player , Matches, Points



@csrf_exempt
@api_view(["GET", "POST"])
def create_team(request):

    """
    #This block of statement will fetch teams data and create new team

    """

    if request.method == "GET":
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        if teams.count() == 0:
            return HttpResponse("No Record Found in Database")
        return HttpResponse(serializer.data, status=200, safe=False)


    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages, status=404)

@api_view(['GET','PUT','DELETE'])
def team_detail(request,id,format=None):

    """
    This block of statement will fetch, update,  delete individual team details
    """

    try:
        obj=Team.objects.get(id=id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=TeamSerializer(obj)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=TeamSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method=="DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "POST"])
def create_player(request):
    """
    #This block of statement will fetch teams data and create new player

    """

    if request.method == "GET":
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        if player.count() == 0:
            return HttpResponse("No Record Found in Database")
        return HttpResponse(serializer.data, status=200, safe=False)


    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PlayerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, id, format=None):
    """
    This block of statement will fetch, update,  delete individual player details
    """

    try:
        obj = Player.objects.get(id=id)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PlayerSerializer(obj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PlayerSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(["GET", "POST"])
def create_match(request):
    """
    #This block of statement will fetch teams data and create new match

    """

    if request.method == "GET":
        match = Matches.objects.all()
        serializer = MatchesSerializer(match, many=True)
        if match.count() == 0:
            return HttpResponse("No Record Found in Database")
        return HttpResponse(serializer.data, status=200, safe=False)


    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = MatchesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def match_detail(request, id, format=None):
    """
    This block of statement will fetch, update,  delete individual matches details
    """

    try:
        obj = Matches.objects.get(id=id)
    except Matches.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = MatchesSerializer(obj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MatchesSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["GET", "POST"])
def create_points(request):
    """
    #This block of statement will fetch teams data and create new match

    """

    if request.method == "GET":
        match = Points.objects.all()
        serializer = PointsSerializer(match, many=True)
        if match.count() == 0:
            return HttpResponse("No Record Found in Database")
        return HttpResponse(serializer.data, status=200, safe=False)


    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = PointsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=201)
        return JsonResponse(serializer.error_messages, status=404)


@api_view(['GET', 'PUT', 'DELETE'])
def points_detail(request, id, format=None):
    """
    This block of statement will fetch, update,  delete individual points details
    """

    try:
        obj = Points.objects.get(id=id)
    except Points.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = PointsSerializer(obj)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PointsSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
