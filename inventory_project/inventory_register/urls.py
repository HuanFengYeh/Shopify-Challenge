from django.urls import path
from inventory_register import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.inventory_form, name='inventory_insert'),
    path('<int:id>/', views.inventory_form, name='inventory_update'),
    path('delete/<int:id>/', views.inventory_delete, name='inventory_delete'),
    path('list/', views.inventory_list, name='inventory_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
