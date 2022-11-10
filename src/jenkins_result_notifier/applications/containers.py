from dependency_injector import containers, providers
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from ..infrastructure.datadog.metrics import DatadogMetricsService

import datadog_api_client


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    metrics_api_client = providers.Selector(
        config.metrics_service,
        datadog=providers.Factory(
            datadog_api_client.ApiClient,
            datadog_api_client.Configuration()
        )
    )
    metrics_service = providers.Selector(
        config.metrics_service,
        datadog=providers.Factory(        
            DatadogMetricsService,
            metrics_api_client
        )
    )
