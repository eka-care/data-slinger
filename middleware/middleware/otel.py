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

def initialize_telemetry():
    resource = Resource(attributes={
        SERVICE_NAME: "medanta_uat",
    })

    # api_key = os.getenv("OTEL_API_KEY")
    headers = (("api-key", "d69e06e854d6f5d5c827dba8a806d5b9c3bdNRAL"),)

    # Metrics Setup
    metric_exporter = OTLPMetricExporter(
        headers=headers,
    )
    reader = PeriodicExportingMetricReader(metric_exporter)

    meter_provider = MeterProvider(resource=resource, metric_readers=[reader])
    set_meter_provider(meter_provider)

    # Tracing Setup
    tracer_provider = TracerProvider(resource=resource)
    span_exporter = OTLPSpanExporter(
        headers=headers,
    )
    span_processor = BatchSpanProcessor(span_exporter)
    tracer_provider.add_span_processor(span_processor)
    trace.set_tracer_provider(tracer_provider)

    DjangoInstrumentor().instrument()
