import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProviderSerializer, ArticleSerializer, PriceSerializer
from .models import Article, Provider, Price

from .models import Article, Provider, Price
from .constants import API_SUCCESS, API_CREATED, API_SERVER_ERR, API_NOT_FOUND, API_BAD_REQUEST

# Create your views here.

@api_view(['GET'])
def index(request):
    price_data = Price.objects.all()
    serializer = PriceSerializer(price_data, many=True)
    API_SUCCESS["data"] = serializer.data
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def article(request):
    request_data = request.data
    if request.method == "POST":
        serializer = ArticleSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            API_CREATED["data"] = [serializer.data]
            return Response(API_CREATED, status=status.HTTP_201_CREATED)

        
        API_SERVER_ERR["data"] = [serializer.errors]
        return Response(API_SERVER_ERR, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        article_id = request.query_params.get("article_id", None)
        
        if article_id:
            try:
                try:
                    article_id = int(article_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                article = Article.objects.get(id=article_id)
                serialized_data = ArticleSerializer(article).data
                
                API_SUCCESS["data"] = [serialized_data]
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
            except Article.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
        elif not article_id:
            articles_data = Article.objects.all()
            serialized_data = ArticleSerializer(articles_data, many=True).data
            API_SUCCESS["data"] = serialized_data
            return Response(API_SUCCESS, status=status.HTTP_200_OK)
        
    if request.method == "PUT":
        article_id = request.query_params.get("article_id", None)
        
        if article_id:
            try:
                try:
                    article_id = int(article_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                article = Article.objects.get(id=article_id)
                serializer = ArticleSerializer(article, data=request_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                
                    API_SUCCESS["data"] = [serializer.data]
                    return Response(API_SUCCESS, status=status.HTTP_200_OK)
                else:
                    API_SERVER_ERR["data"] = serializer.errors
                    return Response(API_SERVER_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Article.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        article_id = request.query_params.get("article_id", None)
        
        if article_id:
            try:
                try:
                    article_id = int(article_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                article = Article.objects.get(id=article_id)
                article.delete()
                API_SUCCESS["data"] = []
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
               
            except Article.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
            
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def provider(request):
    request_data = request.data
    if request.method == "POST":
        serializer = ProviderSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            API_CREATED["data"] = [serializer.data]
            return Response(API_CREATED, status=status.HTTP_201_CREATED)

        API_SERVER_ERR["data"] = [serializer.errors]
        return Response(API_SERVER_ERR, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":
        provider_id = request.query_params.get("provider_id", None)
        
        if provider_id:
            try:
                try:
                    provider_id = int(provider_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                provider = Provider.objects.get(id=provider_id)
                serialized_data = ProviderSerializer(provider).data
                
                API_SUCCESS["data"] = [serialized_data]
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
            except Provider.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
        elif not provider_id:
            provider_data = Provider.objects.all()
            serialized_data = ProviderSerializer(provider_data, many=True).data
            API_SUCCESS["data"] = serialized_data
            return Response(API_SUCCESS, status=status.HTTP_200_OK)
        
    if request.method == "PUT":
        provider_id = request.query_params.get("provider_id", None)
        
        if provider_id:
            try:
                try:
                    provider_id = int(provider_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                provider = Provider.objects.get(id=provider_id)
                serializer = ProviderSerializer(provider, data=request_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                
                    API_SUCCESS["data"] = [serializer.data]
                    return Response(API_SUCCESS, status=status.HTTP_200_OK)
                else:
                    API_SERVER_ERR["data"] = serializer.errors
                    return Response(API_SERVER_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Provider.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        provider_id = request.query_params.get("provider_id", None)
        
        if provider_id:
            try:
                try:
                    provider_id = int(provider_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                provider = Provider.objects.get(id=provider_id)
                provider.delete()
                API_SUCCESS["data"] = []
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
               
            except Provider.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
            
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def price(request):
    request_data = request.data
    entry_id = request.query_params.get("id", None)
    provider_id = request.query_params.get("provider_id", None)
    article_id = request.query_params.get("article_id", None)

    if request.method == "POST":
        serializer = PriceSerializer(data=request_data)
        
        if serializer.is_valid():
            serializer.save()
            API_CREATED["data"] = [serializer.data]
            return Response(API_CREATED, status=status.HTTP_201_CREATED)

        API_SERVER_ERR["data"] = [serializer.errors]
        return Response(API_SERVER_ERR, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == "GET":        
        if provider_id:
            try:
                try:
                    provider_id = int(provider_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                price = Price.objects.filter(provider_id=provider_id)
                serialized_data = PriceSerializer(price, many=True).data
                
                API_SUCCESS["data"] = serialized_data
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
            except Price.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
        if article_id:
            try:
                try:
                    article_id = int(article_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                price = Price.objects.filter(article_id=article_id)
                serialized_data = PriceSerializer(price, many=True).data
                
                API_SUCCESS["data"] = serialized_data
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
            except Price.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
        elif not provider_id and not article_id:
            price_data = Price.objects.all()
            serialized_data = PriceSerializer(price_data, many=True).data
            API_SUCCESS["data"] = serialized_data
            return Response(API_SUCCESS, status=status.HTTP_200_OK)
        
    if request.method == "PUT":        
        if entry_id:
            try:
                try:
                    entry_id = int(entry_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                price = Price.objects.get(id=entry_id)
                serializer = PriceSerializer(price, data=request_data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                
                    API_SUCCESS["data"] = [serializer.data]
                    return Response(API_SUCCESS, status=status.HTTP_200_OK)
                else:
                    API_SERVER_ERR["data"] = serializer.errors
                    return Response(API_SERVER_ERR, status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Price.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":        
        if entry_id:
            try:
                try:
                    entry_id = int(entry_id)
                except Exception as e:
                    API_BAD_REQUEST["data"] = e.__str__()
                    return Response(API_BAD_REQUEST, status.HTTP_400_BAD_REQUEST)
                
                price = Price.objects.get(id=entry_id)
                price.delete()
                API_SUCCESS["data"] = []
                return Response(API_SUCCESS, status=status.HTTP_200_OK)
               
            except Price.DoesNotExist:
                return Response(API_NOT_FOUND, status.HTTP_404_NOT_FOUND)
            
            
    
        
        # if not name:
        #     return JsonResponse(API_SERVER_ERR)
            
        # article = Article.objects.create(id=104, name=name)
        # serialized_data = serialize('json', [article])
        # return JsonResponse(API_CREATED, safe=False, status=201)
    
    
    