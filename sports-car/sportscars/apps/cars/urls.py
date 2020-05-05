from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.cars.views import CreateView, DetailsView, CreateModelInformation, ModelDetailsView

urlpatterns = {
    url(r'^carslist/$', CreateView.as_view(), name="create"),
    url(r'^carslist/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    url(r'^model-information/$', CreateModelInformation.as_view(), name='model-information'),
    url(r'^model-information-update/(?P<pk>[0-9]+)/$', ModelDetailsView.as_view(), name="update_model"),
}
urlpatterns = format_suffix_patterns(urlpatterns)