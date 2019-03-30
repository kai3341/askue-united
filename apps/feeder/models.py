from django.db import models

from apps.consumer import models as consumer


class Feeder(models.Model):
	consumer = models.ForeignKey(
		to=consumer.Consumer,
		on_delete=models.CASCADE,
	)

	name = models.CharField(
		max_length=200,
	)

	def __repr__(self):
		return '<Feeder ' \
			'#{0.id}: ' \
			'"{0.name}" ' \
			'of consumer {0.consumer}' \
		'>'.format(self)

	__str__ = __repr__