from rest_framework import serializers
from . import models


class Consumer(serializers.Serializer):
	class Meta:
		model = models.Consumer

	id = serializers.IntegerField(
		read_only=True,
	)
	name = serializers.CharField(max_length=200)
	contract = serializers.CharField(max_length=200)

	def create(self, validated_data):
		return self.Meta.model.objects.create(**validated_data)

	def update(self, instance, validated_data):
		for key, value in validated_data.items():
			setattr(
				instance,
				key,
				value,
			)
		instance.save()
		return instance
