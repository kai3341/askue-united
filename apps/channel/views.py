from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from . import serializers
from . import models


class Channel(viewsets.ModelViewSet):
	Model = models.Channel
	serializer_class = serializers.Channel
	queryset = Model.objects.all()
	filter_backends = (
		DjangoFilterBackend,
	)
	filterset_fields = (
		'feeder__consumer_id',
		'feeder_id',
	)

	def get_queryset(self):
		get_kwargs = {
			key: value
			for key, value in self.request.GET.items()
			if value
		}

		if get_kwargs:
			return self.queryset.filter(**get_kwargs)
		else:
			return self.queryset.none()
