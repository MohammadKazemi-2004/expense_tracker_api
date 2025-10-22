from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('expense',views.ApiViewsets, basename='expense')
urlpatterns = [
    path('', include(router.urls))
]


# <host>/api/expense/                =>  POST
# <host>/api/expense/<expense id>/  =>  DELETE
# <host>/api/expense/<expense id>/  =>  PUT
# <host>/api/expense/<expense id>/  =>  PATCH
# <host>/api/expense/<expense id>/  =>  GET
# <host>/api/expense/                =>  GET (List endpoint)