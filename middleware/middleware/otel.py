import os

from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.instrumentation.django import DjangoInstrumentor

# Metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.metrics import set_meter_provider

# Tracing
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

def initialize_telemetry(service_name):
    resource = Resource(attributes={
        SERVICE_NAME: service_name,
        "environment": os.getenv("ENVIRONMENT", "developement")
    })

    api_key = os.getenv("OTEL_API_KEY")
    headers = (("api-key", api_key),)

    # Metrics Setup
    metric_exporter = OTLPMetricExporter(
        endpoint=os.getenv("METRICS_ENDPOINT"),
        headers=headers,
        timeout=10
    )
    reader = PeriodicExportingMetricReader(metric_exporter)

    meter_provider = MeterProvider(resource=resource, metric_readers=[reader])
    set_meter_provider(meter_provider)

    # Tracing Setup
    tracer_provider = TracerProvider(resource=resource)
    span_exporter = OTLPSpanExporter(
        endpoint=os.getenv("TRACES_ENDPOINT"),
        headers=headers,
        timeout=10
    )
    span_processor = BatchSpanProcessor(span_exporter)
    tracer_provider.add_span_processor(span_processor)
    trace.set_tracer_provider(tracer_provider)

    DjangoInstrumentor().instrument()
