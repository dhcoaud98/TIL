from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)


class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('actors',)


class ActorSerializer(serializers.ModelSerializer):
    actors_movie = MovieListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)