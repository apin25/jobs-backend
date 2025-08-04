from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.decorators import api_view, authentication_classes
from django.utils import timezone

@authentication_classes([TokenAuthentication])
@api_view(['POST'])
def add_job(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@api_view(['PUT'])
def update_job(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(job, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def get_list_job():
    now = timezone.now()
    jobs = Job.objects.filter(close_at__lte=now)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@api_view(['PUT'])
def close_job(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = request.data.copy()
    data['close_at'] = timezone.now()

    serializer = JobSerializer(job, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_job_detail(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)