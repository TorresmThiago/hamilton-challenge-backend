from django.urls import path
from customers import views

urlpatterns = [
    path('add/', views.customer_add),
    path('list/', views.customer_list),
    path('remove/<int:pk>/', views.customer_remove),
    path('edit/<int:pk>/', views.customer_edit),
]