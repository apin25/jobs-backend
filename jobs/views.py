from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from jobs.models import Job
from jobs.serializers import JobSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.db.models import Q

from utils.authentication import ExpiringTokenAuthentication

@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def add_job(request):
    print("User:", request.user)
    print("Is Authenticated:", request.user.is_authenticated)
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_job(request, id):
    try:
        job = Job.objects.get(id=id, is_deleted=False)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(job, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_list_job(request):
    jobs = Job.objects.filter(is_deleted=False)

    # Satu parameter untuk search
    search = request.query_params.get('search')
    type_of_workplace = request.query_params.get('type_of_workplace')
    employment_type = request.query_params.get('employment_type')

    if search:
        search = search.strip()
        jobs = jobs.filter(
            Q(job_position__icontains=search) |
            Q(company__icontains=search)
        )
    
    if type_of_workplace:
        jobs = jobs.filter(type_of_workplace=type_of_workplace)
    
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)

    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_job(request, id):
    try:
        job = Job.objects.get(id=id)
    except Job.DoesNotExist:
        return Response({"detail": "Job not found."}, status=status.HTTP_404_NOT_FOUND)

    job.is_deleted = True
    job.save()

    return Response({"detail": "Job successfully soft-deleted."}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def get_job_detail(request, id):
    try:
        job = Job.objects.get(id=id, is_deleted=False)
    except Job.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = JobSerializer(job)
    return Response(serializer.data, status=status.HTTP_200_OK)