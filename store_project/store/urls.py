from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Создаём router для API (если используете DRF ViewSets)
router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')  # Пример для ViewSet

urlpatterns = [
    path('', views.home, name='home'),  # Пример обычного view
    path('api/', include(router.urls)),  # Подключаем API URLs
    path('product/<int:pk>/', views.product_detail, name='product-detail'),  # Пример детального view
]

# Если используете Django REST Framework, добавьте:
if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),  # DRF auth для отладки
    ]
