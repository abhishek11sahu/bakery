from django.urls import path
from .views import IngredientsList, IngredientsUpdate, MenuList, MenuCreate, MenuUpdate

urlpatterns = [
    path("ingredients_list/", IngredientsList.as_view()),
    path("ingredients_update/<int:pk>", IngredientsUpdate.as_view()),
    path("menu_list/", MenuList.as_view()),
    path("menu_create/", MenuCreate.as_view()),
    path("menu_update/<int:pk>", MenuUpdate.as_view()),
]