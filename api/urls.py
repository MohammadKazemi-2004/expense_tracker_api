from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('expense',views.ApiViewsets, basename='expense')
urlpatterns = [
    path('', include(router.urls))
]


# <host>/api/etudiants/ POST
# <host>/api/etudiants/<Etudiant id>/ DELETE
# <host>/api/etudiants/<Etudiant id>/ PUT
# <host>/api/etudiants/<Etudiant id>/ PATCH
# <host>/api/etudiants/<Etudiant id>/ GET
# <host>/api/etudiants/ GET (List endpoint)