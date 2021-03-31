from django.urls import path
from .views import index,nextQuestion

urlpatterns=[
    path("",index,name="index"),
    path("<int:k>",nextQuestion,name="next")
]