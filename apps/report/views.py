from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from django.http.response import HttpResponse
from apps.report import mixins


class DataReport(mixins.DataReportMixin,
	viewsets.ReadOnlyModelViewSet):
	pass


class GroupedDataReport(mixins.GroupedReportMixin,
	viewsets.ReadOnlyModelViewSet):
	pass


class FileGroupedDataReport(mixins.FileGroupedReportMixin,
	views.APIView):
	def get(self, request, *args, **kwargs):
		if self.get_crq_kwargs():
			queryset = self.filter_queryset(self.get_queryset())
			response = HttpResponse(
				queryset,
				content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
			)
			response['Content-Disposition'] = 'attachment; filename=download.xlsx'
			return response
		else:
			queryset = [{
				'file': None,
			}]
			serializer = self.serializer_class(queryset, many=True)
			return Response(serializer.data)
