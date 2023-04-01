from rest_framework import serializers
from .models import Blog

class blogPostSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Blog
        fields= (
            'title',
            'content',
            'images',
        )

    def validate_title(self, title):
        if title == '':
            raise serializers.ValidationError("Title cannot be empty")
        return title

    def validate_content(self, content):
        if content == '':
            raise serializers.ValidationError("Content cannot be empty")
        return content

class ListOfBlogs(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id',
            'title',
            'content',
            'images',
        ]

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'images')