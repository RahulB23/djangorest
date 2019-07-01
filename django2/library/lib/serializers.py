from rest_framework import serializers
from lib.models import *


# class UserSer(serializers.Serializer):
#     user_name = serializers.CharField(read_only=True, max_length=64)
#     user_pass = serializers.CharField(read_only=True, max_length=64)
#
#     def create(self, validated_data):
#         return lib.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instace.user_name = validated_data.get('user_name', instance.user_name)
#         instace.user_pass = validated_data.get('user_pass', instance.user_pass)
#         instance.save()
#         return instance


class UserSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_name', 'user_pass',)

class BookSer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('book_name', 'book_quant', 'author')
