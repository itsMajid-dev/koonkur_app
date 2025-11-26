
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_veiws, name='main'),
    # path('run-task/', views.run_task, name='run_task'),
]
