from rest_framework import generics
from twitterapp.models import TweetPost
from twitterapp.api.serializers import TweetPostSerializer

class ListView(generics.ListCreateAPIView):
    queryset = TweetPost.objects.all().order_by('-id')
    serializer_class = TweetPostSerializer
    

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetPost.objects.all()
    serializer_class = TweetPostSerializer