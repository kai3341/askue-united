from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.consumer import views as consumer
from apps.feeder import views as feeder
from apps.channel import views as channel
from apps.datapath import views as datapath
from apps.report import views as report


router = DefaultRouter()

router.register(
	r'consumer',
	consumer.Consumer,
	basename='consumer',
)

router.register(
	r'feeder',
	feeder.Feeder,
	basename='feeder',
)

router.register(
	r'channel',
	channel.Channel,
	basename='channel',
)

router.register(
	r'datapath',
	datapath.Datapath,
	basename='datapath',
)

router.register(
	r'report',
	report.DataReport,
	basename='report',
)

router.register(
	r'grouped-report',
	report.GroupedDataReport,
	basename='grouped_report',
)

#router.register(
#	r'file-grouped-report',
#	report.FileGroupedDataReport,
#	basename='file_grouped_report',
#)


urlpatterns = [
	path('', include(router.urls)),
	path('file-grouped-report/', report.FileGroupedDataReport.as_view()),
]

urlpatterns = [
	path('api/', include(urlpatterns)),
]