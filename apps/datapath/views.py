from rest_framework import viewsets
from . import serializers
from . import models


class Datapath(viewsets.ModelViewSet):
	Model = models.Datapath
	serializer_class = serializers.Datapath
	queryset = Model.objects.all()

	def get_queryset(self):
		return self.queryset.filter(**self.kwargs)
