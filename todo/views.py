from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Todo

class TodosView(APIView):

    def post(self, request):
        todo_name = request.data.get('name', '')
        completed = request.data.get('completed', '')
        
        todo = Todo(
            name=todo_name,
            completed=completed.lower() in ['True', 'true']
        )
        todo.save()

        return JsonResponse({
            "id": todo.id,
            "name": todo.name,
            "completed": todo.completed
        })

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return JsonResponse({
            "id": todo.id,
            "name": todo.name,
            "completed": todo.completed
        })


    def put(self, request, id):
        todo_name = request.data.get('name', '')
        completed = request.data.get('completed', '')

        todo = Todo.objects.get(id=id)
        todo.completed = completed.lower() in ['True', 'true']
        todo.name = todo_name
        todo.save()
        
        return JsonResponse({
            "id": todo.id,
            "name": todo.name,
            "completed": todo.completed
        })

    
