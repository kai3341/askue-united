from django.db import models


class Consumer(models.Model):
	name = models.CharField(
		max_length=200,
	)

	contract = models.CharField(
		max_length=200,
	)

	def __repr__(self):
		return '<Consumer ' \
			'#{0.id}: ' \
			'{0.name}' \
			'{0.contract}' \
		'>'.format(self)

	__str__ = __repr__