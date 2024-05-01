from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def create(self, request, *args, **kwargs):#olustur
        return super().create(request, *args, **kwargs)
    
    
    def list(self, request, *args, **kwargs):#listele
        return super().list(request, *args, **kwargs)
    
    
    def retrieve(self, request, *args, **kwargs):#idye gre listele
        return super().retrieve(request, *args, **kwargs)

    
    def update(self, request, *args, **kwargs):#güncelle
        return super().update(request, *args, **kwargs)

    
    def partial_update(self, request, *args, **kwargs):#kısmen güncelle
        return super().partial_update(request, *args, **kwargs)
    
    
    def destroy(self, request, *args, **kwargs):#sil
        return super().destroy(request, *args, **kwargs)