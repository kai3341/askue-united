from rest_framework.renderers import BaseRenderer, JSONRenderer

class BinaryFileRenderer(BaseRenderer):
	media_type = 'application/octet-stream'
	format = None
	charset = None
	render_style = 'binary'

	def render(self, data, media_type=None, renderer_context=None):
		return data


class ExcelFileRenderer(BinaryFileRenderer):
	media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
