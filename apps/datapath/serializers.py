from rest_framework import serializers
from . import models


class Datapath(serializers.Serializer):
	class Meta:
		model = models.Datapath

	datapath = serializers.CharField()

	def to_representation(self, value):
		return {
			'id': value.id,
			'datapath': str(value),
		}