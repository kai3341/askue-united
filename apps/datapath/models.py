from django.db import models

#from apps.feeder import models as feeder
from apps.datapath import models as datapath


class ConstDatapath(models.Model):
	path = models.CharField(
		max_length=200,
	)

	def __repr__(self):
		return '{0.path}'.format(self)

	__str__ = __repr__


class Datapath(models.Model):
	const_datapath = models.ForeignKey(
		to=datapath.ConstDatapath,
		on_delete=models.CASCADE,
	)

	variable_datapath = models.IntegerField()

	@classmethod
	def add(cls, full_datapath):
		last_dot_index = full_datapath.rindex('.')
		const_datapath = full_datapath[:last_dot_index]
		variable_datapath = full_datapath[last_dot_index+1:]
		variable_datapath = int(variable_datapath)

		const_datapath_record, _ = ConstDatapath.objects.get_or_create(
			path=const_datapath,
		)

		return cls.objects.get_or_create(
			const_datapath=const_datapath_record,
			variable_datapath=variable_datapath,
		)

	def __repr__(self):
		return '{0.const_datapath}.' \
			'{0.variable_datapath}'\
			.format(self)

	__str__ = __repr__
