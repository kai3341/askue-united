from rest_framework import serializers
from . import models


class Feeder(serializers.Serializer):
	class Meta:
		model = models.Feeder

	id = serializers.IntegerField(
		read_only=True,
	)

	name = serializers.CharField()

	def create(self, validated_data):
		get_object = self.context['request'].GET
		get_kwargs = {
			key: get_object[key]
			for key in get_object
		}
		return self.Meta.model.objects.create(
			**validated_data,
			**get_kwargs,
		)

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			setattr(
				instance,
				key,
				value,
			)
		instance.save()
		return instance
