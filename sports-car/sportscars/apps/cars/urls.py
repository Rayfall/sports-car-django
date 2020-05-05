from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.cars.views import CreateView, DetailsView

urlpatterns = {
    url(r'^carslist/$', CreateView.as_view(), name="create"),
    url(r'^carslist/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
}
urlpatterns = format_suffix_patterns(urlpatterns)