from rest_framework import serializers
from apps.channel import models as channel_models
from apps.datapath import models as datapath_models


class Channel(serializers.Serializer):
	class Meta:
		model = channel_models.Channel
		choices = model.choices

	id = serializers.IntegerField(
		read_only=True,
	)

	channel_type = serializers.ChoiceField(
		choices=Meta.choices,
		style={'base_template': 'radio.html'},
		allow_blank=False,
		allow_null=False,
	)

	datapath = serializers.CharField()

	def _prepare(self, validated_data):
		datapath = validated_data['datapath']
		datapath, _ = datapath_models.Datapath.add(datapath)
		validated_data['datapath'] = datapath

	def create(self, validated_data):
		self._prepare(validated_data)

		get_object = self.context['request'].GET
		get_kwargs = {
			key: get_object[key]
			for key in self.context['request'].GET
		}

		return self.Meta.model.objects.create(
			**validated_data,
			**get_kwargs,
		)

	def update(self, instance, validated_data):
		self._prepare(validated_data)
		for key, value in validated_data.items():
			setattr(
				instance,
				key,
				value,
			)
		instance.save()
		return instance
