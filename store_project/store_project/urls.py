from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Админ-панель
    path('admin/', admin.site.urls),
    
    # Маршруты приложения "store"
    path('', include('store.urls')),  # Подключаем URLs из приложения
    
    # API (если используете Django REST Framework)
    path('api/', include('store.urls_api')),  # Пример, если есть отдельный файл для API
]

# Для обслуживания статических файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
