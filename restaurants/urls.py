from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantListView, RestaurantCreateView,
    MainCategoryViewSet, SubCategoryListView,
    SubCategoryDetailView
)

router = DefaultRouter()
router.register(r'restaurants/(?P<restaurant_pk>\d+)/categories',
                MainCategoryViewSet, basename='main-category')

app_name = 'restaurants'

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('subcategories/', SubCategoryListView.as_view(), name='subcategory-list'),
    path('subcategories/<int:pk>/', SubCategoryDetailView.as_view(), name='subcategory-detail'),
    path('', include(router.urls)),
]