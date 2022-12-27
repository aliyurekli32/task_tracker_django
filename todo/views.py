from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method == 'GET':
        ##""""!todos = Todo.objects.all()""""###
        todos = Todo.objects.filter(is_done=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE','PUT'])
def todo_detail(request, pk):
        todo = get_object_or_404(Todo, id=pk)
        if request.method == 'GET':
            #?'todo = Todo.objects.get(id=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer=TodoSerializer(data=request.data, instance=todo)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        elif request.method == 'DELETE':
            todo.delete()
            return Response ({'message':'Updated succesfully'})

