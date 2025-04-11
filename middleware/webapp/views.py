from django.http import HttpResponse

# from .auth import Auth

from opentelemetry import metrics
meter = metrics.get_meter(__name__)

index_view_counter = meter.create_counter(
    name="index_view_requests_total2",
    description="Total number of index view requests",
    unit="1",
)

def index(request):
    index_view_counter.add(1, attributes={"endpoint": "index", "question_count": 1})
    return HttpResponse("Hello")