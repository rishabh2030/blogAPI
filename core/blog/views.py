from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from .models import Blog
from .serializers import blogPostSerializers,ListOfBlogs,BlogSerializer
from rest_framework import generics, status,filters
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
# from django.views.decorators.csrf import csrf_exempt
# from corsheaders.decorators import cors_headers
# from corsheaders.views import cors_exempt
# from django_cors_headers.decorators import cors_exempt


# Create your views here.

class BlogCreate(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = blogPostSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            Blog = serializer.save()
            return Response({'Message': 'Created'}, status = status.HTTP_201_CREATED)
        return Response({'Message':'Error Something went wrong'} , status = status.HTTP_400_BAD_REQUEST)
    
        

# Getting the all list of all blog posted

class BlogPostView(generics.ListAPIView):

    # permission_classes = [IsAuthenticated]    
    serializer_class = ListOfBlogs


    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('search_query',None)
        page_number = request.GET.get('page', 1)
        page_lenght = request.GET.get('page_lenght', 10)

        if search_query:
            queryset = Blog.objects.filter(title__icontains=search_query)
        else:
            queryset = Blog.objects.all()
        
        paginator = Paginator(queryset, page_lenght)  
        page_obj = paginator.get_page(page_number)
        serializer = self.get_serializer(page_obj, many=True).data


        data = {
            "Data":serializer,
            "total_pages": paginator.num_pages,
            "status":"Success",
        }
        return Response(data,status=status.HTTP_200_OK)

# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response

# class BlogPostPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class BlogPostView(generics.ListAPIView):
#     serializer_class = ListOfBlogs
#     pagination_class = BlogPostPagination

#     def get(self, request, *args, **kwargs):
#         search_query = request.GET.get('search_query', None)
#         if search_query:
#             queryset = Blog.objects.filter(title__icontains=search_query)
#         else:
#             queryset = Blog.objects.all()

#         # Paginate the queryset
#         page = self.paginate_queryset(queryset)

#         if page is not None:
#             serializer = self.get_serializer(page, many=True).data
#             return self.get_paginated_response(serializer)

#         serializer = self.get_serializer(queryset, many=True).data
#         data = {
#             "Data": serializer,
#             "status": "Success"
#         }
#         return Response(data, status=status.HTTP_200_OK)

    
# Get blog by id 
class blogPostDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            my_blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogSerializer(my_blog)
        return Response(serializer.data)


# TO delete a blog
class DeleteBlogView(APIView):
    #  permission_classes = [IsAuthenticated]
     def delete(self, request, pk):
        try:
            my_blog = Blog.objects.get(pk=pk)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        my_blog.delete()
        return Response({'message':'Deleted'})

# TO edit the blog
class EditBlogView(APIView):
    # permission_classes = [IsAuthenticated]
    # def put(self, request, *args, **kwargs):
    #     blog_object = Blog.objects.get()

    #     data = request.data
        
    #     blog_object.title = data['title']
    #     blog_object.content = data['content']
    #     blog_object.images = data['images']

    #     blog_object.save()

    #     serializer = blogPostSerializers(blog_object)
    #     return Response(serializer.data)
    def patch(self, request, *args, **kwargs):
        blog_object = Blog.objects.get()

        data = request.data
        
        blog_object.title = data.get("title",blog_object.title)
        blog_object.content = data.get("content",blog_object.content)
        blog_object.images = data.get("images",blog_object.images)

        blog_object.save()

        serializer = blogPostSerializers(blog_object)
        return Response(serializer.data)
    
class SearchBlog(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = Blog.objects.all()
        return queryset
        


        

        
