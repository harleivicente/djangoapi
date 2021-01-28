from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from todo.views import TodosView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/todos", TodosView.as_view()),
    path("api/todos/<int:id>", TodosView.as_view()),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
