from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.getCat),
    path('categories/<int:pk>', views.catRetrieve),
    path('add/', views.addData),
    path('products/', views.getMerch),
    path('products/<int:pk>', views.prodRetrieve),
]