from rest_framework import serializers
from twitterapp.models import TweetPost

class TweetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetPost
        fields = '__all__'