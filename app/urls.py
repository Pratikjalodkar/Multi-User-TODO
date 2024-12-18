from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('signup/', signup, name="signup"),
    path('add-todo/', add_todo), 
    path('delete-todo/<int:id>', delete_todo), 
    path('change-status/<int:id>/<str:status>', change_todo), 
    path('logout/', signout),
]
