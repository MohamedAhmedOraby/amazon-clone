from rest_framework import serializers 
from .models import Product , Brand , ProductReview 



class BrandSerializers (serializers.ModelSerializer) : 
    class Meta : 
        model = Brand 
        fields = '__all__' 


class ProductReviewSerializer (serializers.ModelSerializer) : 
    user = serializers.StringRelatedField
    class Meta : 
        model = ProductReview
        fields = ['id','user','rate','review','date']
        

class ProductListSerializer (serializers.ModelSerializer) : 
    #brand = BrandSerializers () #show all brand details 
    brand = serializers.StringRelatedField #show brand name only 
    class Meta : 
        model = Product 
        fields = '__all__' 

class ProductDetailSerializer (serializers.ModelSerializer) : 
    #brand = BrandSerializers () #show all brand details 
    brand = serializers.StringRelatedField #show brand name only 
    review = ProductReviewSerializer(source='product_review',many=True)
    user = serializers.StringRelatedField
    class Meta : 
        model = Product 
        fields = '__all__' 


class BrandDetailSerializers (serializers.ModelSerializer) : 
    products = ProductListSerializer(source='product_brand',many=True)
    class Meta : 
        model = Brand 
        fields = '__all__' 