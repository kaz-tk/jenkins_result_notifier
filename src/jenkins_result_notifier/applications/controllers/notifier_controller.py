from ...domain.metrics import MetricsService
from ...applications.containers import ApplicationContainer
from dependency_injector.wiring  import Provide, inject

@inject
def notify(metrics_service: MetricsService=Provide[ApplicationContainer.metrics_service]):

    metrics_service.notify()
    pass