from datetime import datetime

from ...domain.metrics import MetricsService

from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_intake_type import MetricIntakeType
from datadog_api_client.v2.model.metric_payload import MetricPayload
from datadog_api_client.v2.model.metric_point import MetricPoint
from datadog_api_client.v2.model.metric_resource import MetricResource
from datadog_api_client.v2.model.metric_series import MetricSeries

from datadog_api_client.v1.api.events_api import EventsApi
from datadog_api_client.v1.model.event_create_request import EventCreateRequest


class DatadogMetricsService(MetricsService):
    def gauge(self):
        metrics_api_client= MetricsApi(self.api_client)

        dynamic_params = {
            "test_name": "get_devices",
            "resource_group": "resource_group_1"
        }

        body = MetricPayload(
            series=[
                MetricSeries(
                    metric=f"jenkins.result.e2e.{dynamic_params['test_name']}",
                    type=MetricIntakeType.GAUGE,
                    points=[
                        MetricPoint(
                            timestamp=int(datetime.now().timestamp()),
                            value=1.0,
                        ),
                    ],
                    resources=[
                        MetricResource(
                            name=dynamic_params['resource_group'],
                            type="host",
                        ),
                    ],
                ),
            ],
        )
        response = metrics_api_client.submit_metrics(body=body)

    def event(self):
        body = EventCreateRequest(
            title="Example-Post_an_event_returns_OK_response",
            text="A text message.",
            tags=[
                "test:ExamplePostaneventreturnsOKresponse",
                "resource_group": "resource_group_1"
            ],
        )
        api_instance = EventsApi(self.api_client)
        response = api_instance.create_event(body=body)
