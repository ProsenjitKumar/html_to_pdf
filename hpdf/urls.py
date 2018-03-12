from django.conf.urls import url
from .views import GeneratePdf

urlpatterns = [
    url(r'^pdf/$', GeneratePdf.as_view()),
]