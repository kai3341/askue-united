import urllib3
import copy
from dateutil import parser
import json
import io
from core.settings import EWS_BACKEND


class EWSReader:
	BACKEND_URL = [
		EWS_BACKEND.rstrip('/'),
		'crq2json',
	]

	http = urllib3.PoolManager()

	deserialization_casts = (
		('date', parser.isoparse),
	)

	__slots__ = (
		'dataset',
		'const_params',
	)

	def __init__(self, dataset, const_params):
		self.dataset = dataset
		self.const_params = const_params

	@classmethod
	def cast_dataset(cls, casts, dataset):
		for row in dataset:
			cls.cast(casts, row)
			yield row

	def full_response(self):
		by_const_datapath = self.group_by_datapath(self.dataset)

		for const_datapath in by_const_datapath:
			params = copy.copy(self.const_params)
			channel_index = {}

			channel_params = by_const_datapath[const_datapath]

			for index, item in enumerate(channel_params):
				crq_channel_index = 'g' + str(index + 1)
				variable_datapath = item['variable_datapath']
				short_channel_name = 'b' + str(variable_datapath)
				params[crq_channel_index] = short_channel_name
				channel_index[variable_datapath] = item

			backend_response = self.get(
				const_datapath,
				params,
			)

			backend_response = io.TextIOWrapper(
				backend_response,
				encoding='utf-8',
			)

			try:
				backend_response = json.load(backend_response)
			except json.JSONDecodeError:
				backend_response = []

			backend_response = self.cast_dataset(
				self.deserialization_casts,
				backend_response,
			)

			backend_response = self.response_mutate(
				backend_response,
				channel_index,
			)

			yield from backend_response

	@classmethod
	def get(cls, const_datapath, params):
		url_datapath = cls.BACKEND_URL + const_datapath.split('.') + ['crq']

		url = '/'.join(url_datapath)

		return cls.http.request(
			method='GET',
			url=url,
			fields=params,
			preload_content=False,
		)

	@staticmethod
	def cast(line_casts, line):
		for key, function in line_casts:
			line[key] = function(line[key])

	@staticmethod
	def response_mutate(parsed_response, channel_index):
		for i in parsed_response:
			channel = i.pop('id')
			channel_info = channel_index[channel]
			i.update(channel_info)
			yield i

	@staticmethod
	def group_by_datapath(datapath):
		by_const_datapath = {}

		for i in datapath:
			const_datapath = i['const_datapath']

			if const_datapath not in by_const_datapath:
				by_const_datapath[const_datapath] = []

			by_const_datapath[const_datapath].append(i)

		return by_const_datapath
