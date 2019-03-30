from rest_framework import viewsets
from apps.consumer import serializers
from apps.consumer import models as consumer_models


class Consumer(viewsets.ModelViewSet):
	serializer_class = serializers.Consumer
	queryset = consumer_models.Consumer.objects.all()
