from rest_framework import serializers

from apps.channel import models as channel_models


class Report(serializers.Serializer):
	class Meta:
		model = channel_models.Channel
		choices = model.choices

	consumer_id = serializers.IntegerField()
	feeder_id = serializers.IntegerField()
	channel_id = serializers.IntegerField()

	channel_type = serializers.ChoiceField(
		choices=Meta.choices,
		style={'base_template': 'radio.html'},
		allow_blank=False,
		allow_null=False,
	)

	const_datapath = serializers.CharField()
	variable_datapath = serializers.IntegerField()

	econom_profile = serializers.IntegerField()
	value = serializers.FloatField()
	date = serializers.DateTimeField()
	valid = serializers.BooleanField()


class GroupedReport(serializers.Serializer):
	class Meta:
		model = channel_models.Channel
		choices = model.choices

	date = serializers.DateTimeField()
	consumer = serializers.ListField()


class FileSerializer(serializers.Serializer):
	file = serializers.FileField()
