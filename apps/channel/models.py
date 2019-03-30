from django.db import models

from apps.feeder import models as feeder
from apps.datapath import models as datapath


class Channel(models.Model):
	choices=tuple(enumerate((
		'A+',
		'A-',
		'R+',
		'R-',
		'QI',
		'QII',
		'QIII',
		'QIV',
	)))

	feeder = models.ForeignKey(
		to=feeder.Feeder,
		on_delete=models.CASCADE,
	)

	datapath = models.ForeignKey(
		to=datapath.Datapath,
		on_delete=models.CASCADE,
	)

	channel_type = models.IntegerField(
		choices=choices,
	)

	def __repr__(self):
		return '<Channel ' \
			'#{self.id}: ' \
			'with datapath "{self.datapath}" ' \
			'of feeder {self.feeder} ' \
			'{channel_type_name}' \
		'>'.format(
			self=self,
			channel_type_name=self.choices[self.channel_type][1],
		)

	__str__ = __repr__

