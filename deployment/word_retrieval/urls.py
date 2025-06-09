from django.urls import path

from . import views

urlpatterns = [
    # ex: /word_retrieval/
    path("", views.index, name="index"),
    # ex: /word_retrieval/results/5/
    path("result/", views.result, name="result"),
]