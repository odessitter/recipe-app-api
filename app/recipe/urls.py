from django.urls import (path, include)
from recipe import views
from rest_framework.routers import DefaultRouter

app_name = 'recipe'
router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
