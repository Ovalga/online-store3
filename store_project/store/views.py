from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Product, Category
from .serializers import ProductSerializer

def home(request):
    """Главная страница со списком товаров."""
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    """Детальная страница товара."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

class ProductViewSet(viewsets.ModelViewSet):
    """API для управления товарами."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """Фильтрация товаров по категории (если указан параметр `category_id`)."""
        queryset = super().get_queryset()
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset
