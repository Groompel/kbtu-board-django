from datetime import datetime

from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=300, default='name')
    description = serializers.CharField(default='')
    creation_date = serializers.DateField(default=datetime.date.today, blank=True)
    user_id = serializers.IntegerField(default=0)
    time = serializers.DateTimeField(default=datetime.now, blank=True)
    place = serializers.CharField(default='')
    photo = serializers.CharField(default='')
    category_id = serializers.IntegerField(default=1)

    def create(self, validated_data):
        post = Post.objects.create(title=validated_data.get('name'),
                                   description=validated_data.get('description'),
                                   creation_date=validated_data.get('creation_date'),
                                   user_id=validated_data.get('user_id'),
                                   time=validated_data.get('time'),
                                   place=validated_data.get('place'),
                                   photo=validated_data.get('photo'),
                                   category_id=validated_data.get('category_id'))
        return post

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
