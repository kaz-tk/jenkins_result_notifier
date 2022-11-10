from ...domain.metrics import MetricsService


class DatadogMetricsService(MetricsService):
    def notify(self):
        print(self.api_client)
        pass
