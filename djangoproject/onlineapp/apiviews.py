from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from onlineapp.models import *
from onlineapp.views import *
from onlineapp.serilalizers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from rest_framework.views import APIView
from onlineapp.views.auth import *


#@basic_authentication
@csrf_exempt
def dislay(request):
    if request.method == 'GET':
        snippets = College.objects.all()
        serializer = CollegeSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = CollegeSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


#@basic_authentication
@csrf_exempt
def modification_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        college = College.objects.get(pk=pk)
    except College.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CollegeSerializer(college)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # import ipdb
        # ipdb.set_trace()
        data = JSONParser().parse(request)
        serializer = CollegeSerializer(college, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        college.delete()
        return HttpResponse(status=204)


#@basic_authentication
class studentlistview(APIView):
    def get_queryset(self):
        return Student.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(college__id=kwargs.get('pk'))
        serializer_class = StudentSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    def post(self, request, pk, format=None):
        request.data.update({'college': pk})
        # import ipdb
        # ipdb.set_trace()
        serializer = StudentDetail(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @basic_authentication
class studentdetailview(APIView):
    def get_queryset(self):
        return Student.objects.all()

    def get(self, request, *args, **kwargs):
        snippets = self.get_queryset().get(pk=kwargs.get('pk'))
        if snippets.college_id == kwargs.get('college_id'):
            mocktest = MockTestMarks.objects.filter(student_id=kwargs.get('pk'))
            snippets.mocktest = mocktest
            serializer = StudentDetail(snippets)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        student = Student.objects.get(id=kwargs.get('pk'))
        # student.mocktest = MockTest1.objects.filter(student_id=kwargs.get('student_id'))

        student.mocktest = MockTestMarks.objects.filter(student_id=kwargs.get('pk'))[0]

        serializer = StudentDetail(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, college_id, format=None):
        student = Student.objects.get(id=pk)
        if student.college_id == college_id:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
