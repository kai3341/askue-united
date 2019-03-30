from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from . import serializers
from . import models


class Feeder(viewsets.ModelViewSet):
	Model = models.Feeder
	serializer_class = serializers.Feeder
	queryset = Model.objects.all()
	filter_backends = (
		DjangoFilterBackend,
	)
	filterset_fields = (
		'consumer_id',
	)

	def get_queryset(self):
		get_object = self.request.GET
		get_kwargs = {
			key: get_object[key]
			for key in get_object
		}

		if get_kwargs:
			return self.queryset.filter(**get_kwargs)
		else:
			return self.queryset.none()
