from django_filters import rest_framework as rest_framework_filters
from apps.consumer import models as consumer_models
from apps.feeder import models as feeder_models
from apps.channel import models as channel_models
from django.forms import widgets


REQ_CHOISES = (
	('archive', 'Archive -- power consumption'),
	('total', 'Total -- cumulative total'),
)

INTERVAL_CHOISES = (
	('short', 'Short interval -- 3 minutes'),
	('main', 'Main interval -- 30 minutes'),
	('day', 'Day interval'),
	('month', 'Month interval'),
	('year', 'Year interval'),
)

TARIFF_CHOISES = (
	('all', 'All'),
	(0, 0),
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
)

class DataReportFilter(rest_framework_filters.FilterSet):
	consumer_id = rest_framework_filters.ModelChoiceFilter(
		queryset=consumer_models.Consumer.objects.all(),
		label='Consumer',
	)

	feeder_id = rest_framework_filters.ModelChoiceFilter(
		queryset=feeder_models.Feeder.objects\
			.select_related()\
			.all(),
		label='Feeder',
	)

	channel_id = rest_framework_filters.ModelChoiceFilter(
		queryset=channel_models.Channel.objects\
			.select_related()\
			.all(),
		label='Channel',
	)

	channel_type = rest_framework_filters.ChoiceFilter(
		choices=channel_models.Channel.choices,
	)

	req = rest_framework_filters.ChoiceFilter(
		choices=REQ_CHOISES,
		field_name=None,
		label='req',
	)

	interval = rest_framework_filters.ChoiceFilter(
		choices=INTERVAL_CHOISES,
		field_name=None,
		label='interval',
	)

	tariff = rest_framework_filters.ChoiceFilter(
		choices=TARIFF_CHOISES,
		field_name=None,
		label='tariff',
	)

	t1 = rest_framework_filters.DateTimeFromToRangeFilter(
		label='t1',
		widget=widgets.DateTimeInput(attrs={
			'placeholder': 'YYYYMMDDHHMMSS',
		})
	)

	t2 = rest_framework_filters.DateTimeFromToRangeFilter(
		label='t2',
		widget=widgets.DateTimeInput(attrs={
			'placeholder': 'YYYYMMDDHHMMSS',
		})
	)

	class Meta:
		model = channel_models.Channel
		fields = [
			'consumer_id',
			'feeder_id',
			'channel_id',
			'channel_type',
			'req',
			'interval',
			'tariff',
			't1',
			't2',
		]